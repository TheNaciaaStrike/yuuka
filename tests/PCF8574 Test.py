from control.modules import PCF8574
import time


test = PCF8574.PCF8574(0x20, 1, 0)


test.write_io(1)
time.sleep(3)
test.write_io(2)
time.sleep(3)
test.write_io(4)
time.sleep(3)
test.write_io(8)
time.sleep(3)
test.write_io(16)
time.sleep(3)
test.write_io(32)
time.sleep(3)
test.write_io(64)
time.sleep(3)
test.write_io(128)
time.sleep(3)
test.write_io(0)
