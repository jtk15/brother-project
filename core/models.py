from django.db import models
from brotherproject.settings import BASE_DIR
from django.conf import settings

class Base(models.Model):
    
    name = models.CharField('Nome', max_length=200)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)
    
    class Meta:
        
        abstract = True
    
    
class Category(Base):
    
    slug = models.CharField(max_length=200, blank=True)
    
    class Meta: 
        
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
        
    def __str__(self):
        return f'Categoria {self.name}'
    
    
class Product(Base):
 
    price = models.DecimalField('Preço', max_digits=6, decimal_places=2)
    title = models.CharField('Titulo', max_length=200, blank=True)
    line = models.CharField('Linha', max_length=200, blank=True)
    image = models.ImageField(upload_to = 'image_uploads/', blank=True)
    category = models.ForeignKey(Category, related_name='categories', on_delete=models.PROTECT, verbose_name='Categoria')
    
    class Meta:

        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return f'Produto {self.name}'


#Vai receber informações gerais sobre o pedido
class OrderManager(models.Manager):
    
    def create_order(self, user, cart_items):
        
        try:
            order = self.create(user=user)
            for cart_item in cart_items:
                
                order_item = OrderItem.objects.create(order=order, product=cart_item.product, quantity=cart_item.quantity, price=cart_item.price)
            
            for cart_item in cart_items:
                cart_item.delete()
            
        except Exception as e:
            pass
    
        return order_item
    
    
class Order(models.Model):
    
    ORDER_STATUS = (
        (0, 'Recebido'),
        (1, 'Aguardando Retirada'),
        (2, 'Cancelado'),
        (3, 'Concluido')
    )
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="orders", on_delete=models.CASCADE)
    status = models.IntegerField('Status do Pedido',  choices=ORDER_STATUS, default=0, blank=False)
    created = models.DateTimeField('Realizado Em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)
    
    objects = OrderManager()
    
    class Meta:
        
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
    
    def __str__(self):
        return 'Pedido #{} ' .format(self.pk)
        

class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name='Pedido do item', related_name='itens', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Produto', related_name='orderitens', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Quantidade', default=1)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=6)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)
    
    class Meta:
        
        verbose_name = 'Item do Pedido'
        verbose_name = 'Itens dos Pedidos'
    
    
    def __str__(self):
        return '{} {}' .format(self.order, self.product)

            