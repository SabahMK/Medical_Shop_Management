from django.contrib import admin
from .models import Bill,Employee

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name','stock']


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['customer','dop']