from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your models here.

class FamilyMember(models.Model):
    name=models.CharField(max_length=255)
    age = models.IntegerField()
    birthdate = models.DateField()
    relatedto = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    phonenumber=models.TextField()
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('familymember_detail', args=[str(self.id)])
class Vehicle(models.Model):
    owner= models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='vehicle')
    number= models.CharField(max_length=25)
    model=models.CharField(max_length=30)
    color=models.CharField(max_length=10)

    def __str__(self):
        return self.number
    # def get_absolute_url(self):
    #     return reverse('article_list')
