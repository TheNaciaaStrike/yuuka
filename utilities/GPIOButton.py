import gpiozero

class GPIOButton:
    def __init__(self, pin):
        self.button = gpiozero.Button(pin)

    def is_pressed(self):
        return self.button.is_pressed

    def when_pressed(self, callback):
        self.button.when_pressed = callback

    def when_released(self, callback):
        self.button.when_released = callback

    def close(self):
        self.button.close()