from django.db import models
from users.models import *
from django.db.models import Sum, F


class Payment(models.Model):
    INACTIVE = 0
    PENDING = 1
    PAY = 2
    STATUS_CHOICES = (
        (INACTIVE, 'inactive'),
        (PENDING, 'pending'),
        (PAY, 'pay'),
    )
    title = models.CharField(max_length=64)
    date_payment = models.DateField()
    employer = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE, related_name='employer_payments')
    employee = models.ManyToManyField(EmployeeProfile, through='EmployeePayment', related_name='employees_payments')
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=PENDING)
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def total_payments(self):
        payment = self.employee_payments_payments.all().aggregate(sum=Sum(F('hour') * F('hourly_wages')))
        return payment.get('sum')


class EmployeePayment(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='employee_payments_payments')
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.DO_NOTHING,
                                 related_name='employee_payments_employees')
    hour = models.PositiveSmallIntegerField(default=1)
    hourly_wages = models.PositiveBigIntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    @property
    def get_total(self):
        return self.hour * self.hourly_wages

    class Meta:
        unique_together = ('payment', 'employee')
