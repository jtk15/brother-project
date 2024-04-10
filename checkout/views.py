from typing import Any
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import RedirectView, TemplateView
from django.forms import modelformset_factory

from .models import CartItem
from  core.models import  Product


class CreateCartItemView(RedirectView):
    
    def get_redirect_url(self, *args, **kwargs):
        
        if self.request.session.session_key is None:
            self.request.session.save()
                
        product = get_object_or_404(Product, pk=kwargs['id'])
        
        CartItem.objects.add_item(self.request.session.session_key, product)
        
        template = self.request.GET.get('uri')
       

        if template == None:
            return '/site/checkout/carrinho'
        else:
            return f'/site/{template}'
 
# class CreateCartItemView(TemplateView):
     
     
#     def get_template_names(self, *args, **kwargs):
        
#         t = self.request.GET.get('t')
        
        
        
#         return [t]
    
    def context_get_data(self, *args, **kwargs):
       
        if self.request.session.session_key is None:
            self.request.session.save()
                
        product = get_object_or_404(Product, pk=kwargs['id'])
        
        CartItem.objects.add_item(self.request.session.session_key, product)
        

class RemoveCartItem(RedirectView):
    
        def get_redirect_url(self, *args, **kwargs): 
            
            product = get_object_or_404(Product, pk=kwargs['id'])
            
            cart_item = CartItem.objects.delete_item(self.request.session.session_key, product)
            
            return '/site/checkout/carrinho'
                        

class CartItemView(TemplateView):
    
    template_name = 'cart.html'
    
    def get_context_data(self,**kwargs):
        
        context = super(CartItemView, self).get_context_data(**kwargs)
    
        ItemCartFomSet = modelformset_factory(
            CartItem, 
            fields=['quantity'],
            extra=0,
            can_delete=True
        )
         
        if self.request.session.session_key is None:
            self.request.session.save()
            
        session_key = self.request.session.session_key
        
        cart_items = CartItem.objects.filter(cart_key=session_key)
        
        cart_price = 0
        for item in  cart_items:
            cart_price = item.price + cart_price
        context['cart_price'] = cart_price
        
        
        
        if session_key:
            context['formset'] = ItemCartFomSet(queryset=cart_items)
        else:
            context['formset'] = ItemCartFomSet(queryset=CartItem.objects.none)
        context['form_valid']=int(len(context['formset']))
          
        return context
    

def  carrinho(request): 
    
    return render(request, 'cart.html') 


remove_cart_item = RemoveCartItem.as_view()
item_cart_view  =  CartItemView.as_view()


