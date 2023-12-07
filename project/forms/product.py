from django import forms
from project.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model: Product
        fields = ['name', 'cas_number', 'purch_price',
                  'purch_cod', 'description', 'brand',
                  'sell_cod', 'sell_price', 'product_type']
    
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        