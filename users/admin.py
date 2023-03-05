from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_staff')
    list_filter = ('is_staff',)
    search_fields = ('username',)


class EmployerAdmin(admin.ModelAdmin):
    list_display = ('username', 'get_is_staff')
    search_fields = ('username',)

    def username(self, obj):
        return obj.user.username

    def get_is_staff(self, obj):
        return obj.user.is_staff


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('username', 'employer')
    search_fields = ('username', 'employer')

    def username(self, obj):
        return obj.user.username

    def employer(self, obj):
        return obj.employer.user.username


admin.site.register(User, UserAdmin)
admin.site.register(EmployerProfile, EmployerAdmin)
admin.site.register(EmployeeProfile, EmployeeAdmin)
