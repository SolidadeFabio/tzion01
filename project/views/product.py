from django.shortcuts import render
from django_htmx.http import retarget
from project.models import Product
from project.forms import ProductForm
from decimal import Decimal
from django.http import JsonResponse

def show_product(request):
    if request.htmx:
        products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request, 'product/show.html', context)
    
def product_json(request):
    products = Product.objects.all()
    data = [product.to_dict_json() for product in products]
    response = {'data': data}
    return JsonResponse(response)
    
def create_product_page(request):
    if request.htmx:
        form = ProductForm()
        context = {
            'form': form
        } 
        return render(request, 'product/create.html', context)
    
    
# ACERTAR O SUPPLIER
def create_product(request):

    if request.method == 'POST':
        
        # name = request.POST.get('name')
        # cas_number = request.POST.get('cas_number')
        # purch_price = request.POST.get('purch_price')
        # purch_cod = request.POST.get('purch_cod')
        # description = request.POST.get('description')
        # brand = request.POST.get('brand')
        # sell_cod = request.POST.get('sell_cod')
        # sell_price = request.POST.get('sell_price')
        # product_type = request.POST.get('product_type')
        # supplier = request.POST.get('supplier')
        
        # name = str(name)
        # cas_number = str(cas_number)
        # purch_price = Decimal(purch_price)
        # purch_cod = str(purch_cod)
        # description = str(description)
        # brand = str(brand)
        # sell_cod = str(sell_cod)
        # sell_price = Decimal(sell_price)
        # product_type = str(product_type)
    
        # product = Product(
        #     name=name,
        #     cas_number=cas_number,
        #     purch_price=purch_price,
        #     purch_cod=purch_cod,
        #     description=description,
        #     brand=brand,
        #     sell_cod=sell_cod,
        #     sell_price=sell_price,
        #     product_type=product_type
        #     )
        # product.save()
        
        form = ProductForm(request.POST)
        
        if form.is_valid():
            form.save()
        
            response = render(request, 'messages/sucess_message.html')
            return retarget(response, '#save_response')
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)

    
    

        

        