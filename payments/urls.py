from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('change_status/<int:pk>', change_payment_status, name='change_payment_status')
]
