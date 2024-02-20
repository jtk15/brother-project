from django.urls import path

from core.views import index, products


urlpatterns = [
    path('index', index),
    path('produtos', products, name='products'),
]