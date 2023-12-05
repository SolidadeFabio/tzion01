from django.db import models
from. supplier import Supplier

class Product(models.Model):
    TYPE_CHOICE = (
        ('national', 'nacional'),
        ('imported', 'importado'),
    )
    description = models.CharField(max_length=255)
    brand = models.CharField(max_length=50)
    sell_cod = models.FloatField()
    purch_cod = models.FloatField()
    cas_number = models.FloatField()
    sell_price = models.DecimalField(max_digits=16, decimal_places=4)
    purch_price = models.DecimalField(max_digits=16, decimal_places=4)
    product_type = models.CharField(max_length=10, choices=TYPE_CHOICE)
    
    supplier = models.ForeignKey(
        Supplier,
        related_name='product',
        on_delete='CASCADE'
    )
    
