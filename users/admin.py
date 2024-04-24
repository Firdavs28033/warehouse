from django.contrib import admin

from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['first_name', 'last_name','username', 'role', 'profile_picture', 'is_staff', ]
    list_filter = ['role', ]
    search_fields = ['first_name', 'last_name', 'username', 'role']
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ('role', 'profile_picture')}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ('role', 'profile_picture')}),)

admin.site.register(User, CustomUserAdmin)