from django.db import models
from plant.models import Plant
from devices.models import ReporterDevice, TemperatureAndHumidityDevice, SoilMoistureDevice, WaterLevelDevice
# Create your models here.




class PlantData(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    humidity = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    reporter = models.ForeignKey(ReporterDevice, on_delete=models.CASCADE)
    device = models.ForeignKey(SoilMoistureDevice, on_delete=models.CASCADE)


    
class TemperatureData(models.Model):
    temperature = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    reporter = models.ForeignKey(ReporterDevice, on_delete=models.CASCADE)
    device = models.ForeignKey(TemperatureAndHumidityDevice, on_delete=models.CASCADE)
   

    
class HumidityData(models.Model):
    humidity = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    reporter = models.ForeignKey(ReporterDevice, on_delete=models.CASCADE)
    device = models.ForeignKey(TemperatureAndHumidityDevice, on_delete=models.CASCADE)


class WaterLevelData(models.Model):
    waterLevel = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)
    reporter = models.ForeignKey(ReporterDevice, on_delete=models.CASCADE)
    device = models.ForeignKey(WaterLevelDevice, on_delete=models.CASCADE)


class LightData(models.Model):
    light = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)
    reporter = models.ForeignKey(ReporterDevice, on_delete=models.CASCADE)


class WindowData(models.Model):
    window = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)
    reporter = models.ForeignKey(ReporterDevice, on_delete=models.CASCADE)

    
