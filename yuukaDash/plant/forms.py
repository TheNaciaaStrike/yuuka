from django.forms import ModelForm
from .models import Plant

# Define your form classes here
class PlantForm(ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'type', 'description','I2CCode','reporter']


