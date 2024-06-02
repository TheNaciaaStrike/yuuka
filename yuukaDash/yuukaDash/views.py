from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.decorators.clickjacking import xframe_options_exempt


# create templace view

class Homepage(TemplateView):
    template_name = 'home.html'
    @xframe_options_exempt
    def get(self, request: HttpRequest, *args: reverse_lazy, **kwargs: reverse_lazy) -> HttpResponse:
        return super().get(request, *args, **kwargs)