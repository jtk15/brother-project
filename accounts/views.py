from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .admin import CustomUserCreationForm

# Create your views here.
def register(request):  
    user_empty_data = {}
    user_data = {}
    field_kyes = ['name', 'surname', 'username', 'email', 'phone', 'password1', 'password2'] #'code', 'address', 'complement']
    
    
    if request.method == 'POST':
        
        datas = request.POST
        
        for key in datas.keys():
            user_data.update({
                key: datas[key]
            })
        
        for key in field_kyes:
            if datas[key] == '':
                user_empty_data[key]=f'Campo Obrigatorio' 

        form = CustomUserCreationForm(request.POST)
    
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro Realizado com Sucesso')
            
        else:
            if request.method == 'POST':
                messages.error(request, 'Formulário Inválido')
            form = CustomUserCreationForm()  
       
          
          
    return render(request, 'registration/register.html', context={'user_empty_data':user_empty_data, 'user_data':user_data})  
