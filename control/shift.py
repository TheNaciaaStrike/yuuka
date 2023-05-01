import digitalio

def shift_update(data, data_pin, clock_pin, latch_pin):
    data_pin = digitalio.DigitalInOut(data_pin)
    data_pin.direction = digitalio.Direction.OUTPUT

    clock_pin = digitalio.DigitalInOut(clock_pin)
    clock_pin.direction = digitalio.Direction.OUTPUT

    latch_pin = digitalio.DigitalInOut(latch_pin)
    latch_pin.direction = digitalio.Direction.OUTPUT
    # put latch down to start data sending
    clock_pin.value = False
    latch_pin.value = False
    clock_pin.value = True
    #print(data)
    # load data in reverse order
    for i in range(15, -1, -1):
        clock_pin.value = False
        data_pin.value = int(data[i])
        clock_pin.value = True

    # put latch up to store data on register
    clock_pin.value = False
    latch_pin.value = True
    clock_pin.value = True
