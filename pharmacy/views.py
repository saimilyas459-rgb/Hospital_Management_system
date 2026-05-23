from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Medicine


@login_required
def medicine_list(request):
    query = request.GET.get('q', '')
    medicines = Medicine.objects.all()
    if query:
        medicines = medicines.filter(name__icontains=query)
    return render(request, 'pharmacy/list.html', {'medicines': medicines, 'query': query})


@login_required
def add_medicine(request):
    if request.method == 'POST':
        Medicine.objects.create(
            name=request.POST['name'],
            company=request.POST['company'],
            price=request.POST['price'],
            stock=request.POST['stock'],
            expiry=request.POST['expiry'],
        )
        messages.success(request, 'Dawa successfully add ho gayi!')
        return redirect('medicine_list')
    return render(request, 'pharmacy/form.html', {'title': 'Naya Dawa Add Karein'})


@login_required
def edit_medicine(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    if request.method == 'POST':
        medicine.name    = request.POST['name']
        medicine.company = request.POST['company']
        medicine.price   = request.POST['price']
        medicine.stock   = request.POST['stock']
        medicine.expiry  = request.POST['expiry']
        medicine.save()
        messages.success(request, 'Dawa update ho gayi!')
        return redirect('medicine_list')
    return render(request, 'pharmacy/form.html', {'medicine': medicine, 'title': 'Dawa Edit Karein'})


@login_required
def delete_medicine(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk)
    medicine.delete()
    messages.warning(request, 'Dawa delete ho gayi.')
    return redirect('medicine_list')
