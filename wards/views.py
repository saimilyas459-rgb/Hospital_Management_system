from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Ward, Bed
from patients.models import Patient


@login_required
def ward_list(request):
    wards = Ward.objects.prefetch_related('bed_set').all()
    return render(request, 'wards/list.html', {'wards': wards})


@login_required
def add_ward(request):
    if request.method == 'POST':
        Ward.objects.create(
            name=request.POST['name'],
            capacity=request.POST['capacity'],
        )
        messages.success(request, 'Ward add ho gaya!')
        return redirect('ward_list')
    return render(request, 'wards/ward_form.html', {'title': 'Naya Ward'})


@login_required
def bed_list(request):
    beds = Bed.objects.select_related('ward', 'patient').all()
    return render(request, 'wards/bed_list.html', {'beds': beds})


@login_required
def add_bed(request):
    if request.method == 'POST':
        Bed.objects.create(
            ward_id=request.POST['ward'],
            bed_no=request.POST['bed_no'],
        )
        messages.success(request, 'Bed add ho gaya!')
        return redirect('bed_list')
    return render(request, 'wards/bed_form.html', {
        'title': 'Naya Bed',
        'wards': Ward.objects.all(),
    })


@login_required
def assign_bed(request, pk):
    bed = get_object_or_404(Bed, pk=pk)
    if request.method == 'POST':
        patient_id = request.POST.get('patient')
        if patient_id:
            bed.patient  = Patient.objects.get(pk=patient_id)
            bed.occupied = True
        else:
            bed.patient  = None
            bed.occupied = False
        bed.save()
        messages.success(request, 'Bed status update ho gayi!')
        return redirect('bed_list')
    return render(request, 'wards/assign.html', {
        'bed': bed,
        'patients': Patient.objects.all(),
    })


@login_required
def free_bed(request, pk):
    bed = get_object_or_404(Bed, pk=pk)
    bed.patient  = None
    bed.occupied = False
    bed.save()
    messages.success(request, f'Bed {bed.bed_no} khali ho gaya!')
    return redirect('bed_list')
