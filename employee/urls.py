from django.urls import path
from . import views

urlpatterns = [
    path('', views.emp_home, name="employee"),
]
