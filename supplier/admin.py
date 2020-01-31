from django.contrib import admin
from .models import Supply
# Register your models here.

@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    list_display = ['name','company','stock']
    