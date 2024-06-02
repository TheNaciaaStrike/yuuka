from django.urls import path

from . import views

urlpatterns = [
    path("", views.ShowAllData.as_view(), name="datalog_list"),
    path("create/temperature", views.TemperatureDataCreateView.as_view(), name="create_temperature_and_humidity_datalog"),
    path("create/humidity/", views.HumidityDataCreateView.as_view(), name="create_humidity_datalog"),
    path("create/soil_moisture/", views.PlantDataCreateView.as_view(), name="create_soil_moisture_datalog"),
]