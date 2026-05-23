from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'speciality', 'phone', 'fee', 'available']
    search_fields = ['name', 'speciality']
    list_filter = ['speciality', 'available']
