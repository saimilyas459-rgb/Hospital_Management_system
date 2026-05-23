from django.contrib import admin
from .models import Ward, Bed

@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'capacity']

@admin.register(Bed)
class BedAdmin(admin.ModelAdmin):
    list_display = ['id', 'bed_no', 'ward', 'patient', 'occupied']
    list_filter = ['occupied', 'ward']
