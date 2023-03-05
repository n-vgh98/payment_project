from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    # path('create_form', create_payment, name='create_payment'),
    path('change_status/<int:pk>', change_payment_status, name='change_payment_status'),
]
