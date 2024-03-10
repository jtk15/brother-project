from django.contrib.auth.forms import UserCreationForm 
from accounts.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
        
    class Meta:
        model = CustomUser
        fields = ['name', 'username', 'email', 'cell_phone', 'password1', 'password2']