from django.urls import path

from core.views import (
    index,
    products,
    products_by_category, 
    promotions, contact, 
    product_detail,
    create_order
)


urlpatterns = [
    path('inicio', index, name='index'),
    path('produtos', products, name='products'),
    path('produtos/detalhes/<int:pk>', product_detail, name='product_detail'),
    path('produtos/<str:slug>', products_by_category, name='products'),
    path('promocoes', promotions, name='promotions'),
    path('contatos', contact, name='contact'),
    path('pedido/fenalizado', create_order, name='finishingorder'),
]