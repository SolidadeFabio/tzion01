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
    
def create_product(request):
    if request.method == 'POST':     
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            response = render(request, 'messages/product-sucess.html')
            return retarget(response, '#save_response')
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        




    
    

        

        