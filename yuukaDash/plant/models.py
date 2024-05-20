from django.db import models
from devices.models import ReporterDevice


# Create your models here.


class Plant(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    description = models.TextField()
    dateAdded = models.DateTimeField(auto_now_add=True)
    I2CCode = models.CharField(max_length=4,null=True, blank=True)
    reporter = models.ForeignKey(ReporterDevice, on_delete=models.CASCADE,null=True, blank=True)

