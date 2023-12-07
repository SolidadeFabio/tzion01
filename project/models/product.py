from django.db import models
from. supplier import Supplier

class Product(models.Model):
    TYPE_CHOICE = (
        ('national', 'nacional'),
        ('imported', 'importado'),
    )
    name = models.CharField(max_length=100, default='')
    cas_number = models.CharField(max_length=100)
    purch_price = models.DecimalField(max_digits=16, decimal_places=4)
    purch_cod = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    brand = models.CharField(max_length=50)
    sell_cod = models.CharField(max_length=50)
    sell_price = models.DecimalField(max_digits=16, decimal_places=4)
    product_type = models.CharField(max_length=10, choices=TYPE_CHOICE)
    created_at = models.DateTimeField(auto_now=True)
    
    supplier = models.ForeignKey(
        Supplier,
        related_name='product',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    
    class Meta:
        ordering = ('name', 'purch_cod')
        verbose_name = 'product'
        verbose_name_plural = 'products'
    
    def __str__(self) -> str:
        return self.name
        
        