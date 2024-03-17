from django.db import models
from django.db import transaction

class ItemMananger(models.Manager):
    
    def add_item(self, cart_key, product):
       
        if self.filter(cart_key=cart_key, product=product).exists():
            created = False
            # with transaction.atomic():
            
            # if cart_item.stock_product > 0:
            cart_item = self.get(cart_key=cart_key, product=product)
            cart_item.quantity = cart_item.quantity  + 1
            print('st :{} qt: {}' .format(cart_item.product.stock_product, cart_item.quantity))
            if cart_item.quantity <= cart_item.product.stock_product:
                
                cart_item.price = cart_item.price + product.price
                cart_item.save()
            else:
                print('Produto com estoque baixo')
        else: 
            created = True
            with transaction.atomic():
                cart_item = CartItem(cart_key=cart_key, product=product, price=product.price)
                cart_item.save() 
            
        return cart_item, created

    def delete_item(self, cart_key, product):
        
            if self.filter(cart_key=cart_key, product=product).exists():
                cart_item = self.get(cart_key=cart_key, product=product)
                
                if(cart_item.quantity < 2):
                    cart_item.delete()
                else:
                    cart_item.quantity -= 1
                    cart_item.price -= product.price 
                    cart_item.save()
            
            return cart_item


class CartItem(models.Model):
    
    cart_key = models.CharField('Chave do Carrinho', max_length=40, db_index=True)
    product = models.ForeignKey('core.Product', related_name='itemcarts', on_delete=models.CASCADE)
    quantity  =  models.PositiveIntegerField('Quantidade', default=1)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=6)
    created = models.DateTimeField('Criado Em', auto_now_add=True)
    modified = models.DateTimeField('Modificado Em', auto_now=True)
    
    objects = ItemMananger()
    
    class Meta:
        
        verbose_name = 'Item do carrinho'
        verbose_name_plural = 'Itens dos carrinhos'
        unique_together = (('cart_key', 'product'))
        
    def __str__(self):
        return '{} [{}]' .format(self.product, self.quantity)
