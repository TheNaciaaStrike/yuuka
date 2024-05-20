import os
from logger.modules import ARDUINIO

arduino = ARDUINIO.ArduinoSerial('/dev/ttyUSB0', 9600)


arduino.connect()

while True:
    arduino.send_i2c_adress("32\n")
    #os.sleep(1)

arduino.disconnect()