from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.

class IOcontorl(TemplateView):
    template_name = 'io.html'