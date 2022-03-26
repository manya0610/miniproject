from socket import fromshare
from django import forms
from .models import Apartment, Building
from accounts.models import CustomUser
class ApartmentForm(forms.ModelForm):
    building=forms.ModelChoiceField(queryset=Building.objects.all())
    apartmentnumber=forms.CharField(label='',widget=forms.Textarea(attrs={'rows':'1','placeholder':'say something'}))
    owner=forms.ModelChoiceField(queryset=CustomUser.objects.all())
    occupied=forms.BooleanField(required=False)
    rentstatus=forms.BooleanField(required=False)

    class Meta:
        model=Apartment
        fields=['building','apartmentnumber','owner','occupied','rentstatus']