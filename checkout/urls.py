from django.urls import path
from .views import crate_cart_item, item_cart_view, remove_cart_item

urlpatterns = [
    path('carrinho/<int:id>', crate_cart_item, name='cartcreate'),
    path('remover/<int:id>', remove_cart_item, name='itemremove'),
    path('carrinho', item_cart_view, name='checkout')
]
 