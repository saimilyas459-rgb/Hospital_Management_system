from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from .models import Bill
from patients.models import Patient


@login_required
def bill_list(request):
    filter_paid = request.GET.get('paid', '')
    bills = Bill.objects.select_related('patient').all()
    if filter_paid == 'yes':
        bills = bills.filter(paid=True)
    elif filter_paid == 'no':
        bills = bills.filter(paid=False)
    total_due = Bill.objects.filter(paid=False).aggregate(total=Sum('amount'))['total'] or 0
    return render(request, 'billing/list.html', {
        'bills': bills,
        'filter_paid': filter_paid,
        'total_due': total_due,
    })


@login_required
def add_bill(request):
    if request.method == 'POST':
        Bill.objects.create(
            patient_id=request.POST['patient'],
            amount=request.POST['amount'],
            description=request.POST['description'],
            paid=request.POST.get('paid') == 'on',
        )
        messages.success(request, 'Bill ban gaya!')
        return redirect('bill_list')
    return render(request, 'billing/form.html', {
        'title': 'Naya Bill Banao',
        'patients': Patient.objects.all(),
    })


@login_required
def edit_bill(request, pk):
    bill = get_object_or_404(Bill, pk=pk)
    if request.method == 'POST':
        bill.patient_id  = request.POST['patient']
        bill.amount      = request.POST['amount']
        bill.description = request.POST['description']
        bill.paid        = request.POST.get('paid') == 'on'
        bill.save()
        messages.success(request, 'Bill update ho gaya!')
        return redirect('bill_list')
    return render(request, 'billing/form.html', {
        'bill': bill,
        'title': 'Bill Edit Karein',
        'patients': Patient.objects.all(),
    })


@login_required
def mark_paid(request, pk):
    bill = get_object_or_404(Bill, pk=pk)
    bill.paid = True
    bill.save()
    messages.success(request, f'Bill #{bill.id} paid mark ho gaya!')
    return redirect('bill_list')


@login_required
def delete_bill(request, pk):
    bill = get_object_or_404(Bill, pk=pk)
    bill.delete()
    messages.warning(request, 'Bill delete ho gaya.')
    return redirect('bill_list')
