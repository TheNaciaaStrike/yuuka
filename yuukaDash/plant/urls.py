from django.urls import path

from . import views

urlpatterns = [
    path("", views.PlantView.as_view(), name="plant_list"),
    path("create/", views.PlantCreateView.as_view(), name="create"),
    #path("<int:plant_id>/", views..as_view(), name="view"),
    path("edit/<int:pk>/", views.PlantUpdateView.as_view(), name="edit_plant"),
    path("delete/<int:pk>/", views.PlantDeleteView.as_view(), name="delete_plant"),
]