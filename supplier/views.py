from django.shortcuts import render
from employee.models import Employee
from medicine.models import Medicine

def supp_home(request):
    return render(request, 'bill.html')


