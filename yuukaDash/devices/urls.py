from django.urls import path

from . import views

urlpatterns = [
    path("reporter/", views.ReporterView.as_view(), name="reporter_list"),
    path("reporter/create/", views.ReporterCreateView.as_view(), name="create_reporter"),
    path("reporter/edit/<int:pk>/", views.ReporterUpdateView.as_view(), name="edit_reporter"),
    path("reporter/delete/<int:pk>/", views.ReporterDeleteView.as_view(), name="delete_reporter"),
    path("temperature_and_humidity/", views.TemperatureAndHumidityDeviceView.as_view(), name="temperature_and_humidity_list"),
    path("temperature_and_humidity/create/", views.TemperatureAndHumidityDeviceCreateView.as_view(), name="create_temperature_and_humidity"),
    path("temperature_and_humidity/edit/<int:pk>/", views.TemperatureAndHumidityDeviceUpdateView.as_view(), name="edit_temperature_and_humidity"),
    path("temperature_and_humidity/delete/<int:pk>/", views.TemperatureAndHumidityDeviceDeleteView.as_view(), name="delete_temperature_and_humidity"),
    path("soil_moisture/", views.SoilMoistureDeviceView.as_view(), name="soil_moisture_list"),
    path("soil_moisture/create/", views.SoilMoistureDeviceCreateView.as_view(), name="create_soil_moisture"),
    path("soil_moisture/edit/<int:pk>/", views.SoilMoistureDeviceUpdateView.as_view(), name="edit_soil_moisture"),
    path("soil_moisture/delete/<int:pk>/", views.SoilMoistureDeviceDeleteView.as_view(), name="delete_soil_moisture"),
]