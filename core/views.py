from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.db import transaction

from checkout.models import CartItem
from core.models import Order, Product
from core.models import Order, Product, Category

##  based-view  class

class CreateOrder(LoginRequiredMixin, TemplateView):
    
    template_name = 'finishing_order.html'
    
    def get(self, request, *args, **kwargs):
            
        session_key = request.session.session_key
        
        if session_key and CartItem.objects.filter(cart_key=session_key).exists():
            cart_items = CartItem.objects.filter(cart_key=session_key)
            
            cart_price = 0
            for item in  cart_items:
                cart_price = item.price + cart_price
        
            with transaction.atomic():
                order = Order.objects.create_order(user=request.user, cart_items=cart_items, order_price=cart_price)
        else:
            return redirect('/site/inicio')
        
        return super(CreateOrder, self).get(request, *args, **kwargs)
    

class OrderViews(TemplateView):
    
    template_name = 'orders.html'
    
    def get_context_data(self, *args, **kwargs):
        user_orders = Order.objects.filter(user=self.request.user)
       
        context = super(OrderViews, self).get_context_data(**kwargs)
        
        for order in user_orders:
            for dic_items in order.itens.values():
                context['items'] = dic_items
                
        context['orders'] = user_orders
        context['products'] = Product.objects.all()
        
        return context


class ContactView(TemplateView):
    
    template_name = 'contact.html'


def index(request):
    
    context  = {
        'products': Product.objects.all()
    }
    
    return render(request, 'home.html', context)


def products(request):
    
    products = None
    
    filter_request = request.GET.get('filter')
   
    if filter_request == None or len(filter_request) == 0:
        products = Product.objects.filter()   
    else:
        products = Product.objects.filter(name__contains=filter_request)

    context = {
        'products': products
    }
    
    return render(request, 'products.html', context)


def products_by_category(request, slug):
    
    products = None

    try:
        
        category = Category.objects.get(slug=slug) 
        
        filter_request = request.GET.get('filter')
        if filter_request == None or len(filter_request) == 0:
            products = category.categories.filter()   
        else:
            products = category.categories.filter(name__contains=filter_request)
        
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


# def promotions(request):
    
    
#     return render(request, 'promotions.html')

