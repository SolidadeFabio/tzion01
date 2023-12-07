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
    quantity = models.IntegerField(default=0)
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
        
    def to_dict_json(self):
        return {
            'pk': self.pk,
            'name': self.name,
            'quantity': self.quantity,
            'cas_number': self.cas_number,
            'purch_price': self.purch_price,
            'purch_cod': self.purch_cod,
            'brand': self.brand,
            'sell_cod': self.sell_cod,
            'sell_price': self.sell_price,
            'product_type': self.product_type,
            'supplier': self.supplier,
        }