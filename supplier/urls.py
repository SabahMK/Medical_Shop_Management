from django.urls import path
from . import views

urlpatterns = [
    path('', views.supp_home, name="supplier"),
]
