from django.contrib import admin
from .models import Medicine




@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ['name', 'customer', 'quantity', 'weight', 'price', 'placed_at']
    



    
