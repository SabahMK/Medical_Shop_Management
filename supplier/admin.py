from django.contrib import admin
from .models import Supplier
from employee.models import Bill

# Register your models here.
class BillInline(admin.TabularInline):
    model = Bill
    extra = 1


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ["contact_person","company","phone", "email","address"]
    inlines = (BillInline,)
