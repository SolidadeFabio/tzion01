from django.contrib import admin
from .models import Product, Supplier


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'name', 'purch_price', 'sell_price', 'description' )
    search_fields = ('purch_cod', 'product_type', 'name')
    list_filter = ('product_type', )
