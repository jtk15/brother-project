from django.contrib import admin
from core.models import Product, Category, Order, OrderItem

class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'category', 'created', 'modified']    
    
    
class AdminCategory(admin.ModelAdmin):
    list_display = ['id', 'name', 'created', 'modified']
    

class OrderItemInline(admin.TabularInline):
    # list_display = ['id', 'order', 'product', 'quantity', 'price']
    # search_fields = ['order']
    model = OrderItem
    extra = 0  # Não mostrar campos vazios
    # readonly_fields = ['product', 'price', 'quantity',]  # Definir o campo title como apenas leitura


class AdminOrder(admin.ModelAdmin):
    list_display = ['id', 'user', 'status', 'order_price', 'created', 'modified']
    search_fields = ['status', 'id']
    
    inlines = [
        OrderItemInline
    ]
    
    
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Order, AdminOrder)
# admin.site.register(OrderItem, OrderItemInline)

