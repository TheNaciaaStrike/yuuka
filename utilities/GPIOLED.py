import gpiozero

class GPIOLED:
    def __init__(self, pin):
        self.led = gpiozero.LED(pin)

    def on(self):
        self.led.on()

    def off(self):
        self.led.off()

    def toggle(self):
        self.led.toggle()

    def close(self):
        self.led.close()