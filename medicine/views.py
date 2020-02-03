from django.shortcuts import render
from supplier.models import Supplier
from employee.models import Employee
from .models import Medicine

def med_home(request):
    all_meds = Medicine.objects.all()
    context = {
        'all_meds' : all_meds,
    }

    return render(request, 'main/medicine.html',context )

def search_medicine(request):
    if request.method == 'POST':
        search_med = request.POST.get('search')
    else:
        search_med = ''
    medicines = Medicine.objects.filter(name__icontains=search_med)
    context = {
        'medicines' : medicines,
    }
    return render(request, 'main/search_medicine.html', context)
