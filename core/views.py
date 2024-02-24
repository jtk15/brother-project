from django.http import HttpResponse
from django.shortcuts import render

from core.models import Product, Category


def index(request):
    
    return render(request, 'base.html')

def products(request):
    
    products = Product.objects.all()
    
    context = {
        'products': products
    }
    
    return render(request, 'products.html', context)


def products_by_category(request, slug):
    
    try:
        category = Category.objects.get(slug=slug) 
        products = category.categories.all()
        
        context = {
            'products': products
        }
        
        return render(request, 'products_by_category.html', context)
    except Category.DoesNotExist:
        
        print('Categoria nao exite')
        
    return render(request, 'products_by_category.html', {'error': "Pagina categoria nao encontrada"})

    
    
