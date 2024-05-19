import smbus

class I2CDevice:
    def __init__(self, address, bus=1):
        self.address = address
        self.bus = smbus.SMBus(bus)

    def write_byte(self, register, value):
        self.bus.write_byte_data(self.address, register, value)

    def read_byte(self, register):
        return self.bus.read_byte_data(self.address, register)

    def write_bytes(self, register, values):
        self.bus.write_i2c_block_data(self.address, register, values)

    def read_bytes(self, register, length):
        return self.bus.read_i2c_block_data(self.address, register, length)
