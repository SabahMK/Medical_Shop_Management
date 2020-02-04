from django.shortcuts import render
from supplier.models import Supplier
from employee.models import Employee
from .models import Medicine
from django.db.models import Q

def med_home(request):
    medicines = Medicine.objects.all()
    context = {
        'medicines' : medicines,
    }

    return render(request, 'main/medicine.html',context )

def search_medicine(request):
    name = request.GET.get('q')
    medicines = Medicine.objects.all().filter(
        (Q(name__icontains=name) &
        Q(quantity__icontains=name) &
        Q(price__icontains=name))
        context = {
        'medicines' : medicines,
    }
    return render(request, 'main/search_medicine.html', context)
