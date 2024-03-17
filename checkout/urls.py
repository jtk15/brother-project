from django.urls import path
from .views import CreateCartItemView, item_cart_view, remove_cart_item

urlpatterns = [
    path('carrinho/<int:id>', CreateCartItemView.as_view(), name='cartcreate'),
    path('remover/<int:id>', remove_cart_item, name='itemremove'),
    path('carrinho', item_cart_view, name='checkout')
]
 