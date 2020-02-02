from django.urls import path
from . import views

urlpatterns = [
    path('', views.med_home, name="medicine"),
    path('search_medicine',views.search_medicine, name="search_medicine"),
]
