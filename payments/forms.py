from django import forms
from .models import *


class CreatePayment(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('title', 'date_payment', 'employer')
