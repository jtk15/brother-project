from django.urls import path

from core.views import (
    index,
    products,
    products_by_category, 
    # promotions,
    product_detail,
    CreateOrder,
    OrderViews,
    ContactView,
    HistoryOrderViews
)


urlpatterns = [
    path('inicio', index, name='index'),
    path('produtos', products, name='products'),
    path('produtos/detalhes/<int:pk>', product_detail, name='product_detail'),
    path('produtos/<str:slug>', products_by_category, name='products'),
    path('produtos/pesquisa/<str:filter', products, name='searchfilter'),
    # path('promocoes', promotions, name='promotions'),
    path('contatos', ContactView.as_view(), name='contact'),
    path('pedido/fenalizado', CreateOrder.as_view(), name='finishingorder'),
    path('pedidos/', OrderViews.as_view(), name='orders'),
    path('pedidos/historico-pedidos', HistoryOrderViews.as_view(), name='history-orders'),
]