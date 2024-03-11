from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser 
from accounts.forms import CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    
    list_display = ['username', 'name', 'email', 'cell_phone']
    
    add_form = CustomUserCreationForm
    readonly_fields = ['created', 'modified']
    fieldsets = (
        ('Informações', {'fields': ('name', 'username', 'email', 'cell_phone')}),
        (None, {'fields': ('created', 'modified')}),
        ('Permissões', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
