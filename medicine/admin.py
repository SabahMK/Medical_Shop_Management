from django.contrib import admin
from .models import Medicine

# Register your models here.
@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity','price','mfd','exp']
    list_display_links = ['name']
    autocomplete_fields = ['name']
