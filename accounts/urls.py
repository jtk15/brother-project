
from django.urls import path
from .views import Register, MyCount
 
 
urlpatterns = [
    path('registro', Register.as_view(), name='register'),
    path('conta', MyCount.as_view(), name='my-count')
]
 