from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from checkout.models import ItemCart

from core.models import Order, Product, Category

##  based-view  class

class CreateOrderView(LoginRequiredMixin, TemplateView):
    
    template_name = 'finishing_order.html'
    
    def get(self, request, *args, **kwargs):
            
        session_key = request.session.session_key
        
        if session_key and ItemCart.objects.filter(cart_key=session_key).exists():
            
            cart_items = ItemCart.objects.filter(cart_key=session_key)
            order = Order.objects.create_order(user=request.user, cart_items=cart_items)
        else:
            return redirect('/site/inicio')
        
        return super(CreateOrderView, self).get(request, *args, **kwargs)
    
    
def index(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')


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


def product_detail(request, pk):
     
    product = Product.objects.get(pk=pk)
    

    context = {
        'product_image': product.image
    }
    
    return render(request, 'product_detail.html', context) 


def promotions(request):
    
    
    return render(request, 'promotions.html')

    
create_order = CreateOrderView.as_view()
