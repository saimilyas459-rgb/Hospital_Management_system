from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Doctor


@login_required
def doctor_list(request):
    query = request.GET.get('q', '')
    doctors = Doctor.objects.all()
    if query:
        doctors = doctors.filter(name__icontains=query)
    return render(request, 'doctors/list.html', {'doctors': doctors, 'query': query})


@login_required
def add_doctor(request):
    if request.method == 'POST':
        Doctor.objects.create(
            name=request.POST['name'],
            speciality=request.POST['speciality'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            fee=request.POST['fee'],
            available=request.POST.get('available') == 'on',
        )
        messages.success(request, 'Doctor successfully add ho gaya!')
        return redirect('doctor_list')
    return render(request, 'doctors/form.html', {'title': 'Naya Doctor Add Karein', 'specialities': Doctor.SPECIALITIES})


@login_required
def edit_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.name      = request.POST['name']
        doctor.speciality= request.POST['speciality']
        doctor.phone     = request.POST['phone']
        doctor.email     = request.POST['email']
        doctor.fee       = request.POST['fee']
        doctor.available = request.POST.get('available') == 'on'
        doctor.save()
        messages.success(request, 'Doctor ki maloomat update ho gayi!')
        return redirect('doctor_list')
    return render(request, 'doctors/form.html', {
        'doctor': doctor,
        'title': 'Doctor Edit Karein',
        'specialities': Doctor.SPECIALITIES
    })


@login_required
def delete_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    doctor.delete()
    messages.warning(request, 'Doctor delete ho gaya.')
    return redirect('doctor_list')
