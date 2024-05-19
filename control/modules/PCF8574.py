#Control module for PCF8574 I2C 8bit IO expander
#Product page: https://www.ti.com/product/PCF8574/part-details/PCF8574N
#Datasheet: https://www.ti.com/lit/ds/symlink/pcf8574.pdf
#Dip package (DW/N package)
#Pinout:
# 1: A0 | Vcc: 16
# 2: A1 | SDA: 15
# 3: A2 | SCL: 14
# 4: P0 | INT: 13
# 5: P1 | P7: 12
# 6: P2 | P6: 11
# 7: P3 | P5: 10
# 8: GND | P4: 9
#I2C Addressing:
# A2 | A1 | A0 | Address
# 0  |  0 |  0 | 0x20
# 0  |  0 |  1 | 0x21
# 0  |  1 |  0 | 0x22
# 0  |  1 |  1 | 0x23
# 1  |  0 |  0 | 0x24
# 1  |  0 |  1 | 0x25
# 1  |  1 |  0 | 0x26
# 1  |  1 |  1 | 0x27
#Usage:
# pcf = PCF8574.PCF8574(0x20, 1)
# pcf.write_io(1)
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../..'))
from utilities.I2C import I2CDevice

class PCF8574(I2CDevice):
    def __init__(self, address, bus=1, inversion=1):
        super().__init__(address, bus)
        self.inverison= inversion

    def read_io(self):
        return self.bus.read_byte(self.address)

    def write_io(self, value):
        if self.inverison!=1 :
            value = ~value
        self.bus.write_byte(self.address, value)
