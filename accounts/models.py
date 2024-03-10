from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUser(AbstractUser):
    
    name = models.CharField('Nome', max_length=30)
    cell_phone = models.CharField('Telefone Celular', max_length=30)
    email = models.EmailField('E-mail', unique=True)
    created = models.DateTimeField('Registrado Em', auto_now_add=True)
    modified = models.DateTimeField('Modificado Em', auto_now=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
    
    
    def __str__(self):
        return self.username
    
    
    
