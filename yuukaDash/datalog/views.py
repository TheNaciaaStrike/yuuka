from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from .models import PlantData, TemperatureData, HumidityData, WaterLevelData, LightData, WindowData
from .forms import PlantDataForm, TemperatureDataForm, HumidityDataForm, WaterLevelDataForm, LightDataForm, WindowDataForm

# Create your views here.

class ShowAllData(TemplateView):
    #model = PlantData
    template_name = 'table.html'
    context_object_name = 'data'
    title = 'Data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #fields = [field.name for field in PlantData._meta.get_fields()]
        context['title'] = self.title
        #context['fields'] = fields
        return context

    #def get(self, request):


class PlantDataCreateView(CreateView):
    model = PlantData
    form_class = PlantDataForm
    template_name = 'form.html'
    success_url = reverse_lazy('data_list')

class TemperatureDataCreateView(CreateView):
    model = TemperatureData
    form_class = TemperatureDataForm
    template_name = 'form.html'
    success_url = reverse_lazy('data_list')

class HumidityDataCreateView(CreateView):
    model = HumidityData
    form_class = HumidityDataForm
    template_name = 'form.html'
    success_url = reverse_lazy('data_list')

class WaterLevelDataCreateView(CreateView):
    model = WaterLevelData
    form_class = WaterLevelDataForm
    template_name = 'form.html'
    success_url = reverse_lazy('data_list')

class LightDataCreateView(CreateView):
    model = LightData
    form_class = LightDataForm
    template_name = 'form.html'
    success_url = reverse_lazy('data_list')

class WindowDataCreateView(CreateView):
    model = WindowData
    form_class = WindowDataForm
    template_name = 'form.html'
    success_url = reverse_lazy('data_list')