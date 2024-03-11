
from django.urls import path
from .views import Register, my_count
 
 
urlpatterns = [
    path('registro', Register.as_view(), name='register'),
    path('conta', my_count.as_view(), name='my-count')
]
 