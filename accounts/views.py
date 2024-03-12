from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import TemplateView

from accounts.forms import CustomUserCreationForm


class MyCount(TemplateView):
    
    template_name = 'registration/my_count.html'
    
    def get_context_data(self, *args, **kwargs):
        
        user = self.request.user
    
        context = super(MyCount, self).get_context_data(*args,**kwargs)
        context['email']=user.email
        context['username']=user.username
        
        return context


class Register(TemplateView):
    
    template_name = 'registration/register.html'
    
    def get_context_data(self, *args, **kwargs):
        
        context = super(Register, self).get_context_data(**kwargs)
    
        return context   
    
    def post(self, request, *args, **kwargs):
        
        user_empty_data = {}
        user_data = {}
        field_kyes = ['name', 'username', 'email', 'cell_phone', 'password1', 'password2']

        if request.method == 'POST':
            
            datas = request.POST
        
            for key in datas.keys():
                user_data.update({
                    key: datas[key]
                })
            
            for key in field_kyes:
                if datas[key] == '':
                    user_empty_data[key]=f'Campo Obrigatorio'
                    
            context = self.get_context_data(**kwargs) 
            context.update({'user_empty_data':user_empty_data, 'user_data':user_data})
           
            form = CustomUserCreationForm(request.POST)
        
            if form.is_valid():
                form.save()
                messages.success(request, 'Cadastro Realizado com Sucesso')
                return redirect('/accounts/registro')
               
            else:
                if request.method == 'POST':
                    messages.error(request, 'Formulário Inválido')
                   
                    return self.render_to_response(context)
