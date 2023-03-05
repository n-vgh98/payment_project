from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


def dashboard(request):
    n = EmployeeProfile.objects.filter(employer=request.user.id)
    if request.method == 'GET':
        payments = Payment.objects.all()
        employees = EmployeeProfile.objects.filter(employer=request.user.id)

        context = {
            'payments': payments,
            'employees': employees,
            'n': n
        }
        return render(request, 'payments/dashboard.html', context)
    elif request.method == 'POST':
        title = request.POST.get('title')
        date_payment = request.POST.get('date_payment')
        user = request.user
        employer = EmployerProfile.objects.get(id=user.id)
        payment_new = Payment.objects.create(
            title=title,
            date_payment=date_payment,
            employer=employer
        )

        employee = request.POST.get('employee')
        hour = request.POST.get('hour')
        hourly_wages = request.POST.get('hourly_wages')
        payment_id = payment_new.id
        EmployeePayment.objects.create(
            payment=Payment.objects.get(id=payment_id),
            employee=EmployeeProfile.objects.filter(id=employee),
            hour=hour,
            hourly_wages=hourly_wages
        )
        return redirect('dashboard')


def change_payment_status(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    if not payment.status == 0:
        payment.status = request.POST.get('status')
        payment.save()

    return redirect('dashboard')
