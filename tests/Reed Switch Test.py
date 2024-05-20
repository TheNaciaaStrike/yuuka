import logger.reedswitch
import time

reed = logger.reedswitch.ReedSwitch(27)

while True:
    print(reed.is_pressed())
    time.sleep(1)