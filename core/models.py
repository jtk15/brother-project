from django.db import models

class Base(models.Model):
    
    name = models.CharField('Nome', max_length=200)
    
    class Meta:
        
        abstract = True
    
    
class Category(Base):
       
    def __str__(self):
        return f'Categoria {self.name}'
    
    
class Product(Base):
 
    price = models.DecimalField('Preço', max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, related_name='categories', on_delete=models.PROTECT)

    def __str__(self):
        return f'Produto {self.name}'
