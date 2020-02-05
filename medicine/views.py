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
    medicines = Medicine.objects.all()
    query = request.GET.get('q')
    if not query == None:
        medicines = Medicine.objects.all().filter(
        Q(name__icontains=query) |
        Q(quantity__icontains=query) &
        Q(price__icontains=query)
    )
    else:
        medicines = Medicine.objects.all()
    context = {
        'medicines' : medicines,
    }
    return render(request, 'main/search_medicine.html', context)
