from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Plant
from .forms import PlantForm

# Create your views here.

class PlantView(ListView):
    model = Plant
    template_name = 'table_plant.html'
    context_object_name = 'plants'
    title = 'Plants'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fields = [field.name for field in Plant._meta.get_fields()]
        context['title'] = self.title
        context['fields'] = fields
        return context

    #def get(self, request):
    #    return HttpResponse("Hello, world. You're at the plant index.")
    

class PlantCreateView(CreateView):
    model = Plant
    form_class = PlantForm
    title = 'Plants'
    template_name = 'form.html'
    success_url = reverse_lazy('plant_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fields = [field.name for field in Plant._meta.get_fields()]
        context['title'] = self.title
        context['fields'] = fields
        return context

class PlantUpdateView(UpdateView):
    model = Plant
    form_class = PlantForm
    title = 'Plants'
    template_name = 'form.html'
    success_url = reverse_lazy('plant_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fields = [field.name for field in Plant._meta.get_fields()]
        context['title'] = self.title
        context['fields'] = fields
        return context

class PlantDeleteView(DeleteView):
    model = Plant
    template_name = 'plant_confirm_delete.html'
    success_url = reverse_lazy('plant_list')
