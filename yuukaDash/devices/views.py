from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ReporterDevice, TemperatureAndHumidityDevice, SoilMoistureDevice
from .forms import ReporterDeviceForm, TemperatureAndHumidityDeviceForm, SoilMoistureDeviceForm

# Create your views here.

class ReporterView(ListView):
    model = ReporterDevice
    template_name = 'table_report.html'
    context_object_name = 'devices'
    title = 'Devices'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fields = [field.name for field in ReporterDevice._meta.get_fields()]
        context['title'] = self.title
        context['fields'] = fields
        return context

    #def get(self, request):

class ReporterCreateView(CreateView):
    model = ReporterDevice
    form_class = ReporterDeviceForm
    template_name = 'form.html'
    success_url = reverse_lazy('reporter_list')
    title = 'Create Device Reporter'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fields = [field.name for field in ReporterDevice._meta.get_fields()]
        context['title'] = self.title
        context['fields'] = fields
        return context

class ReporterUpdateView(UpdateView):
    model = ReporterDevice
    form_class = ReporterDeviceForm
    template_name = 'form.html'
    success_url = reverse_lazy('reporter_list')
    title = 'Edit Device Reporter'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fields = [field.name for field in ReporterDevice._meta.get_fields()]
        context['title'] = self.title
        context['fields'] = fields
        return context

class ReporterDeleteView(DeleteView):
    model = ReporterDevice
    template_name = 'device_confirm_delete.html'
    success_url = reverse_lazy('reporter_list')

class TemperatureAndHumidityDeviceView(ListView):
    model = TemperatureAndHumidityDevice
    template_name = 'table_DHT.html'
    context_object_name = 'devices'
    title = 'Devices'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fields = [field.name for field in TemperatureAndHumidityDevice._meta.get_fields()]
        context['title'] = self.title
        context['fields'] = fields
        return context

    #def get(self, request):

class TemperatureAndHumidityDeviceCreateView(CreateView):
    model = TemperatureAndHumidityDevice
    form_class = TemperatureAndHumidityDeviceForm
    template_name = 'form.html'
    success_url = reverse_lazy('temperature_and_humidity_list')
    title = 'Create Device Temperature and Humidity'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fields = [field.name for field in ReporterDevice._meta.get_fields()]
        context['title'] = self.title
        context['fields'] = fields
        
        return context


class TemperatureAndHumidityDeviceUpdateView(UpdateView):
    model = TemperatureAndHumidityDevice
    form_class = TemperatureAndHumidityDeviceForm
    template_name = 'form.html'
    success_url = reverse_lazy('temperature_and_humidity_list')
    title = 'Edit Device Temperature and Humidity'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fields = [field.name for field in ReporterDevice._meta.get_fields()]
        context['title'] = self.title
        context['fields'] = fields
        return context

class TemperatureAndHumidityDeviceDeleteView(DeleteView):
    model = TemperatureAndHumidityDevice
    template_name = 'device_confirm_delete.html'
    success_url = reverse_lazy('temperature_and_humidity_list')

class SoilMoistureDeviceView(ListView):
    model = SoilMoistureDevice
    template_name = 'table_soil.html'
    context_object_name = 'devices'
    title = 'Devices'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fields = [field.name for field in ReporterDevice._meta.get_fields()]
        context['title'] = self.title
        context['fields'] = fields
        return context

    #def get(self, request):

class SoilMoistureDeviceCreateView(CreateView):
    model = SoilMoistureDevice
    form_class = SoilMoistureDeviceForm
    template_name = 'form.html'
    success_url = reverse_lazy('soil_moisture_list')
    title = 'Create Device Soil Moisture'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fields = [field.name for field in ReporterDevice._meta.get_fields()]
        context['title'] = self.title
        context['fields'] = fields
        return context


class SoilMoistureDeviceUpdateView(UpdateView):
    model = SoilMoistureDevice
    form_class = SoilMoistureDeviceForm
    template_name = 'form.html'
    success_url = reverse_lazy('soil_moisture_list')
    title = 'Edit Device Soil Moisture'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fields = [field.name for field in ReporterDevice._meta.get_fields()]
        context['title'] = self.title
        context['fields'] = fields
        return context

class SoilMoistureDeviceDeleteView(DeleteView):
    model = SoilMoistureDevice
    template_name = 'device_confirm_delete.html'
    success_url = reverse_lazy('soil_moisture_list')
