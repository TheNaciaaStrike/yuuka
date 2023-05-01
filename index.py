#load config.json and print its contents
import json
import adafruit_dht
import board, digitalio
import time, datetime
import threading, os, subprocess 
from gpiozero import CPUTemperature
#import internal modules 
import analyze
from db import pg
from logger import dht, arduino
from control import shift, gpio

with open('config.json') as json_data_file:
    data = json.load(json_data_file)
print (data['i2c'])

bindata = 0b1111111111111111
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
            time.sleep(15)
        except RuntimeError as error:
            print(error)
        except Exception as error:
            dhtDevice.exit()
        
        

def startAnalysis():
    global bindata
    last_run = None
    with open('last_run.txt', 'r') as f:
        last_run_str = f.read().strip()
        if last_run_str:
            last_run = datetime.datetime.fromisoformat(last_run_str)

    while True:
        now = datetime.datetime.now()
        if last_run is None or now.date() > last_run.date():
            # new day, reset all addresses
            bindata = 0b1111111111111111
            #bindata = bindata - bin(int(1)
        elif last_run.time() < datetime.time(11, 0) <= now.time() <= datetime.time(11, 30):
            # during the 11-11:30 time window
            addresses = analyze.analyise_soil()
            print(addresses)
            if addresses:
                for address in addresses:
                    print('in for loop' + str(address))
                    if address == 21:
                        board.D17.value = True
                        time.sleep(5)  # wait for 5 seconds
                        board.D17.value = False
                    elif address == 22:
                        bindata &= 0b0100000000000000
                    elif address == 23:
                        bindata &= 0b0010000000000000
                    elif address == 24:
                        bindata &= 0b0001000000000000
                    elif address == 25:
                        bindata &= 0b0000100000000000
                    elif address == 26:
                        bindata &= 0b0000010000000000
                    elif address == 27:
                        bindata &= 0b0000001000000000
                    elif address == 28:
                        bindata &= 0b0000000100000000
                    else:
                        bindata &= 0b0000000000000000

        last_run = now
        with open('last_run.txt', 'w') as f:
            f.write(last_run.isoformat())
        time.sleep(30)

        bindata = 0b1111111111111111
        print("Shift Registers " +str(bin(bindata)))
                    

        #needed, sunrise, sunset = analyze.light(data['location'])
        #current_time = datetime.now()
        #if needed:
        #    time_before_sunset = datetime.datetime.combine(datetime.date.today(), sunset) - datetime.timedelta(hours=1)
        #    if current_time >= time_before_sunset.time() and current_time <= datetime.time(23, 0) and total_light < 10:
        #        gpio.UV_IR_TOGGLE(board.D12, 1)
        #        total_light += 1
        #    if current_time >= datetime.time(23, 0):
        #        gpio.UV_IR_TOGGLE(board.D12, 0)


def gpioLoop():
    bindata = 0b1111111111111111
    bin_data = str(bin(bindata)[2:].zfill(16))
    shift.shift_update(bin_data,board.D21,board.D16,board.D20)

def get_cpu_temperature():
    res = subprocess.check_output(["vcgencmd", "measure_temp"]).decode("utf-8")
    return float(res.replace("temp=","").replace("'C\n",""))

#Arduino + I2C Log thread
arduinoThread = threading.Thread(target=arduino_log)
arduinoThread.start()
print("started Arduino logging")
#DHT Log thread
DHTThread = threading.Thread(target=dht_log)
DHTThread.start()
#Analyis thread
analysisThread = threading.Thread(target=startAnalysis)
analysisThread.start()
print("started Analysis")

while True:
    bin_data = str(bin(bindata)[2:].zfill(16))
    #print (bin_data)
    shift.shift_update(str(bin(bindata)[2:].zfill(16)),board.D21,board.D16,board.D20)


#test()
# num = 0b00000000011111111
# while num <= 0b1111111111111111:
#     bin_data = str(bin(num)[2:].zfill(16))
#     shift.shift_update(bin_data,board.D21,board.D16,board.D20)
#     num = (num << 1) | 1
#     time.sleep(1)

#gpio.UV_IR_TOGGLE(board.D12,5)
