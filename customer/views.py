from django.shortcuts import render
from customer.models import Customer
from medicine.models import Medicine

def home(request):
    all_medicines = Medicine.objects.all()

    context = {
        'all_medicines' : all_medicines,
    }
    return render(request, 'main/index.html', context)