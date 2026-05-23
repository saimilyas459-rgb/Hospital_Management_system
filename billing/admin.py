from django.contrib import admin
from .models import Bill

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'amount', 'paid', 'date']
    list_filter = ['paid']
    search_fields = ['patient__name']
