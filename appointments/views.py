from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Appointment
from patients.models import Patient
from doctors.models import Doctor


@login_required
def appointment_list(request):
    status_filter = request.GET.get('status', '')
    appointments = Appointment.objects.select_related('patient', 'doctor').all()
    if status_filter:
        appointments = appointments.filter(status=status_filter)
    return render(request, 'appointments/list.html', {
        'appointments': appointments,
        'status_filter': status_filter,
    })


@login_required
def add_appointment(request):
    if request.method == 'POST':
        Appointment.objects.create(
            patient_id=request.POST['patient'],
            doctor_id=request.POST['doctor'],
            date=request.POST['date'],
            time=request.POST['time'],
            reason=request.POST['reason'],
            status='Pending',
        )
        messages.success(request, 'Appointment book ho gayi!')
        return redirect('appointment_list')
    return render(request, 'appointments/form.html', {
        'title': 'Naya Appointment',
        'patients': Patient.objects.all(),
        'doctors': Doctor.objects.filter(available=True),
    })


@login_required
def edit_appointment(request, pk):
    appt = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appt.patient_id = request.POST['patient']
        appt.doctor_id  = request.POST['doctor']
        appt.date       = request.POST['date']
        appt.time       = request.POST['time']
        appt.reason     = request.POST['reason']
        appt.status     = request.POST['status']
        appt.save()
        messages.success(request, 'Appointment update ho gayi!')
        return redirect('appointment_list')
    return render(request, 'appointments/form.html', {
        'appt': appt,
        'title': 'Appointment Edit Karein',
        'patients': Patient.objects.all(),
        'doctors': Doctor.objects.filter(available=True),
        'statuses': Appointment.STATUS_CHOICES,
    })


@login_required
def delete_appointment(request, pk):
    appt = get_object_or_404(Appointment, pk=pk)
    appt.delete()
    messages.warning(request, 'Appointment cancel ho gayi.')
    return redirect('appointment_list')
