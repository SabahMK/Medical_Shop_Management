from django.shortcuts import render
from medicine.models import Medicine
from supplier.models import Supplier
from .models import Employee


def emp_home(request):
    all_employee = Employee.objects.all()
    
    context = {
        'all_employee' : all_employee,
    }
    return render(request, 'main/index.html', context)