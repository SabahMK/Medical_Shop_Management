from django.urls import path
from . import views

urlpatterns = [
    path('', views.med_home, name="medicine"),
]
