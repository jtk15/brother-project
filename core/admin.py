from django.contrib import admin
from core.models import Product, Category

class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'category']
    
    
    

class AdminCategory(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
