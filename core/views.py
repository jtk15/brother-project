from django.http import HttpResponse
from django.shortcuts import render

from core.models import Product


def index(request):
    
    return render(request, 'base.html')

def products(request):
    
    products = Product.objects.all()
    
    context = {
        'products': products
    }
    
    return render(request, 'products.html', context)
