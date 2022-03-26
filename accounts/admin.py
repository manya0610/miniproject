# accounts/admin.py
from re import search
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from family.models import FamilyMember, Vehicle

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display= ['email','username','age','is_staff',]
#     fieldsets= UserAdmin.fieldsets + (
#         (None, {'fields': ('age','phonenumber')}),
#     )
#     add_fieldsets= UserAdmin.add_fieldsets + (
#         (None, {'fields':('age','phonenumber')}),
#     )
# admin.site.register(CustomUser, CustomUserAdmin)

class FamilyMemberInline(admin.TabularInline): # new
    model = FamilyMember
    extra=0
class cua(admin.ModelAdmin):
    inlines = [
    FamilyMemberInline,
    ]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display= ['username','email','age','is_staff',]
    fieldsets= UserAdmin.fieldsets + (
        (None, {'fields': ('age','phonenumber')}),
    )
    add_fieldsets= UserAdmin.add_fieldsets + (
        (None, {'fields':('age','phonenumber')}),
    )
    search_fields=['username','email','age','phonenumber']
admin.site.register(CustomUser,cua)
