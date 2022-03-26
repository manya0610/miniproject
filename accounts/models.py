# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    phonenumber=models.CharField(max_length=255,null=True)

