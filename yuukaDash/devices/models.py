from django.db import models
 
# Create your models here.

class ReporterDevice(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    dateAdded = models.DateTimeField(auto_now_add=True)
    wifi_enabled = models.BooleanField(null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True,unique=True)
    serial_enabled = models.BooleanField(null=True, blank=True)
    serial_port = models.CharField(max_length=200, null=True, blank=True)
    serial_baudrate = models.IntegerField(null=True, blank=True)

class TemperatureAndHumidityDevice(models.Model):
    connectedTo = models.ForeignKey(ReporterDevice, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    i2c_enabled = models.BooleanField(null=True, blank=True)
    i2c_address = models.IntegerField(null=True, blank=True)
    spi_enabled = models.BooleanField(null=True, blank=True)
    spi_address = models.IntegerField(null=True, blank=True)
    gpio_enabled = models.BooleanField(null=True, blank=True)
    gpio_pin = models.IntegerField(null=True, blank=True)

class SoilMoistureDevice(models.Model):
    connectedTo = models.ForeignKey(ReporterDevice, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    i2c_enabled = models.BooleanField(null=True, blank=True)
    i2c_address = models.IntegerField(null=True, blank=True)
    gpio_enabled = models.BooleanField(null=True, blank=True)
    gpio_pin = models.IntegerField(null=True, blank=True)

class WaterLevelDevice(models.Model):
    connectedTo = models.ForeignKey(ReporterDevice, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    i2c_enabled = models.BooleanField(null=True, blank=True)
    i2c_address = models.IntegerField(null=True, blank=True)
    gpio_enabled = models.BooleanField(null=True, blank=True)
    gpio_pin = models.IntegerField(null=True, blank=True)

