from django.contrib import admin
from .models import Building, Apartment


class ApartmentInline(admin.TabularInline): # new
    model = Apartment
    extra=0
class BuildingAdmin(admin.ModelAdmin): # new
    inlines = [
    ApartmentInline,
    ]


# Register your models here.
admin.site.register(Building,BuildingAdmin)
admin.site.register(Apartment)