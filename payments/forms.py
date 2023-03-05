from django import forms
from .models import *
from django.contrib import admin


class ChoiceInline(admin.TabularInline):
    model = EmployeePayment
    extra = 3


class CreatePaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['title', 'date_payment']
        inlines = [ChoiceInline]
