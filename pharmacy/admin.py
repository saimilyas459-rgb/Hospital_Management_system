from django.contrib import admin
from .models import Medicine

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'company', 'price', 'stock', 'expiry']
    search_fields = ['name', 'company']
    list_filter = ['company']
