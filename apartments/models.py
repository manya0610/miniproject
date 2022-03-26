from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your models here.

class Building(models.Model):
    name=models.CharField(max_length=255)

    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('building_detail', args=[str(self.id)])
class Apartment(models.Model):
    building= models.ForeignKey(Building,on_delete=models.CASCADE,related_name='apartment')
    apartmentnumber= models.CharField(max_length=255)
    owner=models.ForeignKey(get_user_model(),on_delete=models.DO_NOTHING,related_name='owner')
    occupied=models.BooleanField(default=False)
    rentstatus=models.BooleanField(default=False)

    def __str__(self):
        return self.apartmentnumber
    def get_absolute_url(self):
        return reverse('building_list')
