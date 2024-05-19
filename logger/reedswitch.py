import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
from utilities.GPIOButton import GPIOButton


class ReedSwitch(GPIOButton):
    def __init__(self, pin):
        super().__init__(pin)

    def on_pressed(self):
        print('Pressed')

    def on_released(self):
        print('Released')