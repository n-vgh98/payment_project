from django.contrib import admin
from .models import *


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('title', 'employer', 'total_payments', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'employer')

    def get_employer(self, obj):
        return obj.employer.user.username


class EmployeePaymentAdmin(admin.ModelAdmin):
    list_display = ('payment', 'employer', 'employee', 'get_total')
    search_fields = ('payment', 'employee')

    def employee(self, obj):
        return obj.employee.user.username

    def employer(self, obj):
        return obj.employee.employer.user.username


admin.site.register(Payment, PaymentAdmin)
admin.site.register(EmployeePayment, EmployeePaymentAdmin)
