from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)


class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class EmployeeProfile(models.Model):
    employer = models.ForeignKey(EmployerProfile, on_delete=models.DO_NOTHING, related_name='employer_employees')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
