from django.urls import path
from . import views

urlpatterns = [
    path('', views.bill_list, name='bill_list'),
    path('add/', views.add_bill, name='add_bill'),
    path('edit/<int:pk>/', views.edit_bill, name='edit_bill'),
    path('paid/<int:pk>/', views.mark_paid, name='mark_paid'),
    path('delete/<int:pk>/', views.delete_bill, name='delete_bill'),
]
