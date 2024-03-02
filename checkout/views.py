from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views.generic import RedirectView, TemplateView
from django.forms import modelformset_factory

from .models import ItemCart 
from  core.models import Product


class CreateCartItemView(RedirectView):
    
    def get_redirect_url(self, *args, **kwargs):
        
        if self.request.session.session_key is None:
            self.request.session.save()
                
        product = get_object_or_404(Product, pk=kwargs['id'])
        
        cart_item = ItemCart.objects.add_item(self.request.session.session_key, product)
        
        return '/site/checkout/carrinho'
    

class RemoveCartItem(RedirectView):
    
        def get_redirect_url(self, *args, **kwargs): 
            
            product = get_object_or_404(Product, pk=kwargs['id'])
            
            cart_item = ItemCart.objects.delete_item(self.request.session.session_key, product)
            
            return '/site/checkout/carrinho'
                        

class CartItemView(TemplateView):
    
    template_name = 'cart.html'
    
    def get_context_data(self,**kwargs):
        
        context = super(CartItemView, self).get_context_data(**kwargs)
    
        ItemCartFomSet = modelformset_factory(
            ItemCart, 
            fields=['quantity'],
            extra=0,
            can_delete=True
        )
       
        session_key = self.request.session.session_key 
        
        if session_key:
            context['formset'] = ItemCartFomSet(queryset=ItemCart.objects.filter(cart_key=session_key))
        else:
            context['formset'] = ItemCartFomSet(queryset=ItemCart.objects.none)
       
        context['form_valid']=int(len(context['formset']))
        
        return context
    

def  carrinho(request): 
    
    return render(request, 'cart.html') 


crate_cart_item = CreateCartItemView.as_view()
remove_cart_item = RemoveCartItem.as_view()
item_cart_view  =  CartItemView.as_view()


