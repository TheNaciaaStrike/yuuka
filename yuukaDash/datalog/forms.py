from django.forms import ModelForm
from .models import PlantData, TemperatureData, HumidityData, WaterLevelData, LightData, WindowData

# Define your form classes here
class PlantDataForm(ModelForm):
    class Meta:
        model = PlantData
        fields = ['plant', 'humidity', 'reporter', 'device']

class TemperatureDataForm(ModelForm):
    class Meta:
        model = TemperatureData
        fields = ['temperature', 'reporter', 'device']

class HumidityDataForm(ModelForm):
    class Meta:
        model = HumidityData
        fields = ['humidity', 'reporter', 'device']

class WaterLevelDataForm(ModelForm):
    class Meta:
        model = WaterLevelData
        fields = ['waterLevel', 'reporter', 'device']

class LightDataForm(ModelForm):
    class Meta:
        model = LightData
        fields = ['light', 'reporter']

class WindowDataForm(ModelForm):
    class Meta:
        model = WindowData
        fields = ['window', 'reporter']

