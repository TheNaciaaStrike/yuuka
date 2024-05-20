from control.modules import SN74HC595
import time

test = SN74HC595.SN74HC595(12, 16, 20, 1)

counter = 0
while True:

    test.shift_out(counter)
    time.sleep(0.1)
    counter += 1
    if counter > 255:
        counter = 0