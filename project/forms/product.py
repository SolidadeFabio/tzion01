from django import forms
from project.models import Product, Supplier


class ProductForm(forms.ModelForm):
    
    field_names_pt = {
        'name': 'Nome',
        'cas_number': 'Número CAS',
        'purch_price': 'Preço de Compra',
        'purch_cod': 'Código de Compra',
        'description': 'Descrição',
        'brand': 'Marca',
        'sell_cod': 'Código de Venda',
        'sell_price': 'Preço de Venda',
        'product_type': 'Tipo de Produto',
        'supplier': 'Fornecedor',
        'quantity': 'Quantidade'
    }
    
    class Meta:
        model = Product
        fields = ['name', 'cas_number', 'purch_price',
                  'purch_cod', 'description', 'brand',
                  'sell_cod', 'sell_price', 'product_type', 
                  'supplier', 'quantity', 'quantity_type']
    
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['aria-describedby'] = 'basic-addon1'
            if field_name == 'supplier':
                field.widget.attrs['placeholder'] = 'Fornecedor'
                field.choices = [('', 'Fornecedor')] + [(supplier.pk, str(supplier.name)) for supplier in Supplier.objects.all().order_by('name')]
                
            if field_name == 'quantity':
                field.widget.attrs['placeholder'] = 'Quantidade'
            
            if field_name =='quantity_type':
                field.widget.attrs['placeholder'] = 'Tipo Quantidade'
                field.choices = [
                    ('', 'Tipo Quantidade'),
                    ('UN', 'UN'),
                    ('PK', 'PK'),
                ]
            
            else:
                field.widget.attrs['placeholder'] = self.field_names_pt.get(field_name, field_name)
            
            if field_name == 'product_type':
                field.widget.attrs['placeholder'] = 'Tipo Produto'
                field.choices = [
                            ('', 'Tipo Produto'),
                            ('NATIONAL', 'Nacional'),
                            ('IMPORTED', 'Importado')
                        ]
            
                    
                
                
