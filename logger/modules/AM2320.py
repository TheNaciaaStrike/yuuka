#Data logger class for AM2320 Temperature and Humidity Sensor
#Product: https://www.adafruit.com/product/3721
#Datasheet: https://cdn-shop.adafruit.com/product-files/3721/AM2320.pdf
#Pinout:
# 1: VCC 3.3 - 5V
# 2: SDA (I2C Data)
# 3: GND
# 4: SCL (I2C Clock)
#I2C Addressing: 0x5C (Default Cannot be changed)
#Timing between readings: 2 seconds
#Usage:
# sensor = AM2320.AM2320()
# sensor.read()
# print(str(sensor.temperature) + " degrees C")
# print(str(sensor.humidity) + " %R\n")
import os
import fcntl
import time


class AM2320:
    def __init__(self, i2c_bus=1, i2c_address=0x5c):
        self.i2c_bus = i2c_bus
        self.i2c_address = i2c_address
        self.fd = os.open(f"/dev/i2c-{self.i2c_bus}", os.O_RDWR)
        fcntl.ioctl(self.fd, 0x0703, self.i2c_address)

        self.raw_data = [0,0,0,0]

        self.temperature = 0
        self.humidity = 0
        self.crc = 0XFFFF
    
    def read(self):
        self.crc = 0xFFFF

        #Check if sensor is not in sleep mode
        try:
            os.write(self.fd, b'\0x00')
        except:
            pass
        #Ask for Temperature and Humidity
        os.write(self.fd, b'\x03\x00\x04')
        #Let the sensor process the data
        time.sleep(0.0001)
        self.raw_data = os.read(self.fd, 8)

        #Data Validation using CRC
        for byte in self.raw_data[0:6]:
            self.crc = self.crc ^ byte
            for _ in range(8):
                if self.crc & 0x01:
                    self.crc = (self.crc >> 1) ^ 0xA001
                else:
                    self.crc = self.crc >> 1
        if self.crc != self.raw_data[7] << 8 | self.raw_data[6]:
            raise Exception("CRC Error")
        elif self.raw_data[0] != 0x03 or self.raw_data[1] != 0x04:
            raise Exception("Data Error")
        else:
            self.temperature = (self.raw_data[4] << 8 | self.raw_data[5])
            #Temperature is 16-bit signed integer check if it is negative
            if (self.temperature & 0x80) == 0x80:
                self.temperature = self.temperature & 0x7FF
            self.temperature = self.temperature / 10
            #Humidity is 16-bit unsigned integer and is always positive
            self.humidity = (self.raw_data[2] << 8 | self.raw_data[3]) / 10
