from django.shortcuts import render
from customer.models import Customer
from medicine.models import Medicine

def home(request):
    
    return render(request, 'main/index.html')

