#Data Logging with Arduino type boards such as UNO, Nano, Mega or other Arduino IDE compatible boards
#With Ability to Send and Receive Serial Data
#Using USB interface
#Possible use of UART interface (Unknown if working)


import serial
import time

class ArduinoSerial:
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.serial = None

    def connect(self):
        try:
            self.serial = serial.Serial(self.port, self.baudrate, timeout=1)
            print("Connected to Arduino on port", self.port)
        except serial.SerialException as e:
            print("Failed to connect to Arduino:", str(e))

    def disconnect(self):
        if self.serial:
            self.serial.close()
            print("Disconnected from Arduino")

    def send_data(self, data):
        if self.serial:
            self.serial.write(data.encode())
            print("Sent data:", data)
        else:
            print("Not connected to Arduino")

    def read_data(self):
        if self.serial:
            data = self.serial.readline().decode('utf-8').rstrip()
            print("Received data:", data)
            return data
        else:
            print("Not connected to Arduino")
    
    def send_i2c_adress(self, data):
        if self.serial:
            self.serial.write(data.encode())
            time.sleep(1.1)
            responce = self.serial.readline().decode('utf-8').rstrip()
            print(responce)
            return responce
        else:
            print("Not connected to Arduino")

