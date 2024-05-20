from django.forms import ModelForm
from .models import ReporterDevice, TemperatureAndHumidityDevice, SoilMoistureDevice, WaterLevelDevice

# Define your form classes here
class ReporterDeviceForm(ModelForm):
    class Meta:
        model = ReporterDevice
        fields = ['name', 'description','wifi_enabled', 'ip_address','serial_enabled','serial_port','serial_baudrate']

class TemperatureAndHumidityDeviceForm(ModelForm):
    class Meta:
        model = TemperatureAndHumidityDevice
        fields = ['connectedTo','name', 'description','i2c_enabled', 'i2c_address','spi_enabled','spi_address','gpio_enabled','gpio_pin']

class SoilMoistureDeviceForm(ModelForm):
    class Meta:
        model = SoilMoistureDevice
        fields = ['connectedTo','name', 'description','i2c_enabled', 'i2c_address','gpio_enabled','gpio_pin']

class WaterLevelDeviceForm(ModelForm):
    class Meta:
        model = WaterLevelDevice
        fields = ['connectedTo','name', 'description','i2c_enabled', 'i2c_address','gpio_enabled','gpio_pin']



