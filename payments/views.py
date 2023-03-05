from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


def dashboard(request):
    if request.method == 'GET':
        payments = Payment.objects.all()
        context = {
            'payments': payments
        }
        return render(request, 'payments/dashboard.html', context)
    if request.method == 'POST':
        title = request.POST.get('title')
        date_payment = request.POST.get('date_payment')
        user = request.user
        employer = EmployerProfile.objects.get(id=user.id)
        Payment.objects.create(
            title=title,
            date_payment=date_payment,
            employer=employer
        )
        return redirect('dashboard')


def change_payment_status(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    Payment.objects.update(
        title=payment.title,
        date_payment=payment.date_payment,
        status=request.POST.get('status')
    )
    return redirect('dashboard')
