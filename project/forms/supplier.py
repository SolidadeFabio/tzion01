from django import forms
from project.models import Supplier

class SupplierForm(forms.ModelForm):
    
    class Meta:
        model = Supplier
        field = ['cnpj']
    