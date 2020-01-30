from django.shortcuts import render
from supplier.models import Supplier
from employee.models import Employee
from .models import Medicine

def med_home(request):
    return render(request, 'main/medicine.html' )

def search_medicine(request):
    if request.method == 'POST':
        search_med = request.POST.get('search')
    else:
        search_med = ''
    medicine = Medicine.objects.filter(name__icontains=search_med)
    context = {
        'medicine' : medicine,
    }
    return render(request, 'main/index.html', context)