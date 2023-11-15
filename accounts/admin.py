from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserModel

from .forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.


# class CustomUserAdmin(UserAdmin):
#     model = CustomUserModel
#     list_display = ['email', 'username', 'first_name', 'last_name',
#                     'dob', 'date_joined', 'is_staff', 'is_superuser']
#     search_fields = ['username', 'email']
#     readonly_fields = ['date_joined', 'last_login']
#     ordering = ['-date_joined']

#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()

class CustomUserAdmin(UserAdmin):
    model = CustomUserModel

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    list_display = ['email', 'username', 'first_name', 'last_name',
                    'dob', 'date_joined', 'is_staff', 'is_superuser']
    ordering = ['-date_joined']

    filter_horizontal = ()

    search_fields = ['username', 'email']
    list_filter = ('is_staff', 'is_superuser')

    fieldsets = (
        ('Main Info', {'fields': ('email', 'password')}),
        ('Personal Info', {
         'fields': ('username', 'first_name', 'last_name', 'dob', 'profile_picture')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'password1', 'password2', 'dob', 'profile_picture', 'is_staff', 'is_admin')
        }),
    )


admin.site.register(CustomUserModel, CustomUserAdmin)
