from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm 

# Create your views here.
def register(request):  
    
    if request.POST == 'POST':  
        form = UserCreationForm()  
        if form.is_valid():  
            form.save()
            print('correto')  
    else:          
        print('error')
        form = UserCreationForm()  
          
          
    return render(request, 'registration/register.html')  
