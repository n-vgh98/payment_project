from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


def dashboard(request):
    if request.method == 'GET':
        payments = Payment.objects.all()
        employees = EmployeeProfile.objects.filter(employer=request.user.id)
        context = {
            'payments': payments,
            'employees': employees
        }
        return render(request, 'payments/dashboard.html', context=context)
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
        payment = payment_new.id
        print(type(payment))
        EmployeePayment.objects.create(
            payment=Payment.objects.get(id=payment),
            employee=EmployeeProfile.objects.get(id=employee),
            hour=hour,
            hourly_wages=hourly_wages
        )
        return redirect('dashboard')


# def create_payment(request):
#     if request.method == 'GET':
#         form = CreatePaymentForm()
#         return render(request, 'payments/form.html', {'form':form})


def change_payment_status(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    Payment.objects.update(
        title=payment.title,
        date_payment=payment.date_payment,
        status=request.POST.get('status')
    )
    return redirect('dashboard')
