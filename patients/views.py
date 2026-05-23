from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Patient
from doctors.models import Doctor
from appointments.models import Appointment
from billing.models import Bill
from pharmacy.models import Medicine
from wards.models import Bed


@login_required
def dashboard(request):
    context = {
        'total_patients':     Patient.objects.count(),
        'total_doctors':      Doctor.objects.count(),
        'total_appointments': Appointment.objects.count(),
        'unpaid_bills':       Bill.objects.filter(paid=False).count(),
        'low_stock':          Medicine.objects.filter(stock__lte=10).count(),
        'empty_beds':         Bed.objects.filter(occupied=False).count(),
        'recent_patients':    Patient.objects.order_by('-registered')[:6],
        'today_appointments': Appointment.objects.filter(status='Pending').order_by('date')[:5],
    }
    return render(request, 'dashboard.html', context)


@login_required
def patient_list(request):
    query = request.GET.get('q', '')
    patients = Patient.objects.all()
    if query:
        patients = patients.filter(name__icontains=query)
    return render(request, 'patients/list.html', {'patients': patients, 'query': query})


@login_required
def add_patient(request):
    if request.method == 'POST':
        Patient.objects.create(
            name=request.POST['name'],
            age=request.POST['age'],
            gender=request.POST['gender'],
            phone=request.POST['phone'],
            address=request.POST['address'],
            blood_group=request.POST['blood_group'],
        )
        messages.success(request, 'patient successfully register!')
        return redirect('patient_list')
    return render(request, 'patients/form.html', {'title': 'Add new patient'})


@login_required
def edit_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.name        = request.POST['name']
        patient.age         = request.POST['age']
        patient.gender      = request.POST['gender']
        patient.phone       = request.POST['phone']
        patient.address     = request.POST['address']
        patient.blood_group = request.POST['blood_group']
        patient.save()
        messages.success(request, 'Marz ki maloomat update ho gayi!')
        return redirect('patient_list')
    return render(request, 'patients/form.html', {'patient': patient, 'title': 'Add new patient'})


@login_required
def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    patient.delete()
    messages.warning(request, 'The disease has been deleted.')
    return redirect('patient_list')
