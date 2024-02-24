from django.urls import path

from core.views import index, products, products_by_category, promotions, contact


urlpatterns = [
    path('inicio', index, name='index'),
    path('produtos', products, name='products'),
    path('produtos/<str:slug>', products_by_category, name='products'),
    path('promocoes', promotions, name='promotions'),
    path('contatos', contact, name='contact'),
]