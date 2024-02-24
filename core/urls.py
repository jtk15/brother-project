from django.urls import path

from core.views import index, products, products_by_category 


urlpatterns = [
    path('index', index),
    path('produtos', products, name='products'),
    path('produtos/<str:slug>', products_by_category, name='products'),
]