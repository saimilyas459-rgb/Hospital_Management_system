from django.urls import path
from . import views

urlpatterns = [
    path('', views.ward_list, name='ward_list'),
    path('add/', views.add_ward, name='add_ward'),
    path('beds/', views.bed_list, name='bed_list'),
    path('beds/add/', views.add_bed, name='add_bed'),
    path('beds/assign/<int:pk>/', views.assign_bed, name='assign_bed'),
    path('beds/free/<int:pk>/', views.free_bed, name='free_bed'),
]
