import gpiozero

class SN74HC595():
    def __init__(self, data, latch, clock, amount=1):
        self.data = gpiozero.LED(data)
        self.latch = gpiozero.LED(latch)
        self.clock = gpiozero.LED(clock)
        self.amount = amount

    def shift_out(self, value):
        for i in range(8* self.amount):
            self.data.value = (value >> i) & 1
            self.clock.on()
            self.clock.off()
        self.latch.on()
        self.latch.off()