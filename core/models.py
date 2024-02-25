from django.db import models
from brotherproject.settings import BASE_DIR

class Base(models.Model):
    
    name = models.CharField('Nome', max_length=200)
    
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
