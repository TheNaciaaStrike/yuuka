import reedswitch
import time

reed = reedswitch.ReedSwitch(27)

while True:
    print(reed.is_pressed())
    time.sleep(1)