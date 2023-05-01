import adafruit_dht
import digitalio


def get_dht_data(dhtDevice_pin):
    # Initial the dht device, with data pin connected to:
    dhtDevice = adafruit_dht.DHT22(dhtDevice_pin)
    # Print the values to the serial port
    try:
        return dhtDevice.temperature, dhtDevice.humidity
    except RuntimeError as error:
        print(error)
    except Exception as error:
        dhtDevice.exit()
