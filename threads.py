from datetime import datetime, time
import time as t
from control import gpio
from logger import dht, arduino
from db import pg
from astral.sun import sun
from astral import LocationInfo
import board, adafruit_dht
import analyze 
import os, subprocess, json


def get_cpu_temperature():
    res = subprocess.check_output(["vcgencmd", "measure_temp"]).decode("utf-8")
    return float(res.replace("temp=","").replace("'C\n",""))

def get_sunrise_sunset(location):
    loc = LocationInfo(location['city'], location['country'])
    s = sun(loc.observer, date=datetime.now())
    sunrise = s['sunrise'].time()
    sunset = s['sunset'].time()
    return sunrise, sunset


def lightloop(data):
    print(data)
    while True:
        try:
            sunrise, sunset = get_sunrise_sunset(data)
            current_time = datetime.now(tz=None).time()
            #if sunrise is not on 7:00 than turn on light till sunrise
            if current_time < sunrise:
                gpio.UV_IR_TOGGLE(board.D12, 0)
            #if sunset is not on 19:00 than turn on light till 22:00
            elif current_time >= sunset and current_time < time(22, 0):
                gpio.UV_IR_TOGGLE(board.D12, 1)
            else:
                gpio.UV_IR_TOGGLE(board.D12, 0)
            t.sleep(60)
        except Exception as e:
            print(e)

def dht_log():
    dhtDevice = adafruit_dht.DHT22(board.D26)
    while True:
        conn = pg.connect()
        # Print the values to the serial port
        try:
            rpitemp = get_cpu_temperature()
            temp = dhtDevice.temperature
            humidity = dhtDevice.humidity
            print("Temperature "+str(temp)+"C")
            print("Humidity "+str(humidity)+"RH")
            print("RPI Temperature "+str(rpitemp)+"C")
            query = "INSERT INTO temperature (\"dhtTemperature\", \"dhtHumidity\", \"rpiTemperature\") VALUES (%s, %s, %s);"
            params = (temp, humidity,rpitemp)
            pg.execute_insert(conn, query,params)
            t.sleep(15)
        except RuntimeError as error:
            print(error)
        except Exception as error:
            dhtDevice.exit()

def arduino_log():
    while True:
        conn = pg.connect()
        try:   
            arduino_log_data = arduino.getSerialData()
            arduinoJson = json.loads(arduino_log_data)
            
            # Check for 65535 in Soil Humid key
            if "Soil Humid" in arduinoJson and arduinoJson["Soil Humid"] == 65535:
                # Get the previous and next readings
                query = "SELECT \"i2cStore\" FROM \"i2cData\" WHERE \"i2cStore\"->>'Time' < %s ORDER BY \"i2cStore\"->>'Time' DESC LIMIT 1;"
                params = (arduinoJson["Time"],)
                result = pg.execute_select(conn, query, params)
                prev_reading = result[0][0]["Soil Humid"] if result else None
                
                query = "SELECT \"i2cStore\" FROM \"i2cData\" WHERE \"i2cStore\"->>'Time' > %s ORDER BY \"i2cStore\"->>'Time' ASC LIMIT 1;"
                params = (arduinoJson["Time"],)
                result = pg.execute_select(conn, query, params)
                next_reading = result[0][0]["Soil Humid"] if result else None
                
                # Approximate the reading from its neighbors
                if prev_reading is not None and next_reading is not None:
                    arduinoJson["Soil Humid"] = round((prev_reading + next_reading) / 2)
                elif prev_reading is not None:
                    arduinoJson["Soil Humid"] = prev_reading
                elif next_reading is not None:
                    arduinoJson["Soil Humid"] = next_reading
            
            query = "INSERT INTO \"i2cData\" (\"i2cStore\") VALUES (%s);"
            params = (json.dumps(arduinoJson),)
            pg.execute_insert(conn, query,params)
        except TypeError:
            print("Ardiono not working")
        except json.JSONDecodeError:
            print("JSON BORK")