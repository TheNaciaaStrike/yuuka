from control.modules import SN74HC595, PCF8574
from logger.modules import AM2320, ARDUINIO
from logger import reedswitch
import time
import db
import logging
import logging.config
import threading

logging.config.fileConfig('logging.conf')

logger = logging.getLogger('main')

#shift_register = SN74HC595.SN74HC595(12, 16, 20, 1)
pcf = PCF8574.PCF8574(0x20, 1,0)
pcf2 = PCF8574.PCF8574(0x21, 1)

counter_shft = 0
counter_pcf = 0

am2320 = AM2320.AM2320()

reed = reedswitch.ReedSwitch(27)


def reed_loop():
    last_reed_state = False
    while True:
        if reed.is_pressed() != last_reed_state:
            last_reed_state = reed.is_pressed()
            logger.info("Reed Switch: " + str(last_reed_state))


def am2320_loop():
    while True:
        try:
            am2320.read()
            logger.debug(str(am2320.temperature) + " degrees C" + " " + str(am2320.humidity) + " %R")
            time.sleep(1)
        except RuntimeError as error:
            logger.warning(error)
        except OSError as error:
            logger.warning("os RRR")
        except Exception as error:
            logger.error(error)
        except KeyboardInterrupt:
            exit(0)
        time.sleep(1)

am2320_thread = threading.Thread(target=am2320_loop)
#am2320_thread.start()

reed_thread = threading.Thread(target=reed_loop)
#reed_thread.start()

#am2320_thread.join()
#reed_thread.join()

try:
    while True:
        #shift_register.shift_out(counter_shft)
        pcf.write_io(counter_pcf)
        pcf2.write_io(counter_pcf)
        #counter_shft += 1
        counter_pcf += 1
        #if counter_shft > 255*shift_register.amount:
        #    counter_shft = 0
        if counter_pcf > 255:
            counter_pcf = 0
        time.sleep(0.5)
    #get keyboaard interrupt
except KeyboardInterrupt:
    print("KeyboardInterrupt")
except OSError as error:
    print("OSError")

