import digitalio

def UV_IR_TOGGLE(pin, mode):
    pin = digitalio.DigitalInOut(pin)
    pin.direction = digitalio.Direction.OUTPUT
    if mode == 0:
        pin.value = False
    elif mode == 1:
        pin.value = True
    else:
        print("WRONG PARAM")