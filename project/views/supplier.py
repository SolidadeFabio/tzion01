from django.shortcuts import render
from django_htmx.http import retarget
from project.utils import consulta_cnpj_api
from project.models import Supplier

def create_supplier(request):
    if request.method == 'POST':
        
        cnpj = request.POST.get('cnpj')
        name = request.POST.get('razao_social')
        
        if not name:
            try:
                cnpj = cnpj.replace('.', '')
                cnpj = cnpj.replace('/', '')
                cnpj = cnpj.replace('-', '')
                enterprise_name = consulta_cnpj_api(cnpj)
                supplier = Supplier(
                    cnpj=cnpj,
                    name=enterprise_name
                )
                supplier.save()
                response = render(request, 'messages/supplier_sucess.html')
                return retarget(response, '#save-supplier')
            except:
                response = render(request, 'messages/supplier_failed.html')
                return retarget(response, '#save-supplier')