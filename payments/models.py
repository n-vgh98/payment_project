from django.db import models
from users.models import *
from django.db.models import Sum


class Payment(models.Model):
    title = models.CharField(max_length=64)
    date_payment = models.DateField()
    employer = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE, related_name='employer_payments')
    employee = models.ManyToManyField(EmployeeProfile, through='EmployeePayment', related_name='employees_payments')
    status = models.BooleanField(default=False)  # False is pending/ True is success
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    @property
    def total_payments(self):
        payment = self.employee_payments_payments.all().aggregate(sum=Sum('get_total'))
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
