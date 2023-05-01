import serial
import time
import json

arduino = serial.Serial("/dev/ttyACM0")
arduino.baudrate=9600

def getSerialData():
    time.sleep(10)
    data = arduino.readline()
    decoded = data.decode('ISO-8859-1').strip()
    print(decoded)
    return decoded
