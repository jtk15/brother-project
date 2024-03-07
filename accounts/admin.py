from django.contrib import admin
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    
    name = forms.CharField(label='Nome', max_length=100)
    surname = forms.CharField(label='Sobre Nome', max_length=100)
    email = forms.EmailField(max_length=100)
    phone = forms.CharField(label='Telefone', max_length=100)
    code = forms.CharField(label='Cep', max_length=11, required=False)
    address = forms.CharField(label='Endereço', max_length=200, required=False)
    complement = forms.CharField(label='Complemento', max_length=200, required=False)
    
    
    class Meta:
        
        model = User
        fields = ('name', 'surname', 'username', 'email', 'phone', 'password1', 'password2', 'code', 'address', 'complement')
