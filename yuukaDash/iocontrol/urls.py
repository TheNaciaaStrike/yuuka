from django.urls import path

from . import views

urlpatterns = [
    path("", views.IOcontorl.as_view(), name="iocontrol"),
]
