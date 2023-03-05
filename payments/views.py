from django.shortcuts import render, redirect
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
        pass

