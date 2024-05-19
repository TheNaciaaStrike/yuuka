#load config.json and print its contents
import json
import board, digitalio
import time, datetime
import threading 
from flask import Flask, jsonify, request
#import internal modules 
import analyze
from db import pg
from control import shift, gpio
import threads as th


with open('config.json') as json_data_file:
    data = json.load(json_data_file)
print (data['i2c'])

app = Flask(__name__)

bindata = 0b1111111111111111    

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


def gpioLoop():
    global bindata
    bin_data = str(bin(bindata)[2:].zfill(16))
    shift.shift_update(bin_data,board.D21,board.D16,board.D20)


def hbrige():
    window_open, window_close = board.D4 , board.D17
    door_open, door_close = board.D27, board.D22
    while True:
        #get last 50 data from db
        conn = pg.connect()
        query = "SELECT * FROM \"temperature\" LIMIT 50;"
        result = pg.execute_query(conn, query)
        #chekc if dhtTemperature is on avarage than higher than 35
        temp = 0
        print(datetime.now().time())
        for row in result:
            temp += row[1]
        temp = temp / 50
        if temp > 35:
            #open window
            gpio.UV_IR_TOGGLE(window_open, 0)
            time.sleep(5)
            gpio.UV_IR_TOGGLE(window_open, 1)
        #check if dhtTemperature is on avarage than lower than 20 or time is 22:00
        elif temp < 20 or datetime.now().time() >= datetime.time(22, 0):
            #close window
            gpio.UV_IR_TOGGLE(window_close, 0)
            time.sleep(5)
            gpio.UV_IR_TOGGLE(window_close, 1)
        


@app.route('/')
def index():
    return 'hello world'

@app.route('/api/shiftregister', methods=['GET', 'POST'])
def shiftregister():
    global bindata
    if request.method == 'POST':
        new_bindata = request.form.get('bindata')
        if new_bindata:
            bindata = int(new_bindata, 2)
        return jsonify({'status': 'success'})
    else:
        return jsonify({'bindata': format(bindata, '016b')})
    


def app_run():
    app.run(host='0.0.0.0', port=8080, debug=False)

#Arduino + I2C Log thread
arduinoThread = threading.Thread(target=th.arduino_log)
arduinoThread.start()
print("started Arduino logging")
#DHT Log thread
DHTThread = threading.Thread(target=th.dht_log)
DHTThread.start()
print("started DHT logging")
#Analyis thread
analysisThread = threading.Thread(target=startAnalysis)
analysisThread.start()
print("started Analysis")
#Light thread
lightThread = threading.Thread(target=th.lightloop,args=(data['location'],))
lightThread.start()
print("started Light")
#Shift Register thread
shiftThread = threading.Thread(target=gpioLoop)
shiftThread.start()
print("started Shift Register")
#Hbridge thread
hbridgeThread = threading.Thread(target=hbrige)
hbridgeThread.start()
print("started Hbridge")

#Web App thread
flaksThread = threading.Thread(target=app_run)
flaksThread.start()

while True:
    #check if threds are still running
    #time.sleep(1)
    bin_data = str(bin(bindata)[2:].zfill(16))
    #print (bin_data)
    shift.shift_update(str(bin(bindata)[2:].zfill(16)),board.D21,board.D16,board.D20)

