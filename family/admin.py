from django.contrib import admin
from .models import FamilyMember,Vehicle
from accounts.models import CustomUser



class FamilyMemberInline(admin.TabularInline): # new
    model = FamilyMember
class VehicleInline(admin.TabularInline): # new
    model=Vehicle
# class UserAdmin(admin.ModelAdmin):
#     inline=[FamilyMemberInline,VehicleInline]

# Register your models here.
# admin.site.register(CustomUser,UserAdmin)
admin.site.register(Vehicle)
admin.site.register(FamilyMember)