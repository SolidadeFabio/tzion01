from django.shortcuts import render, get_object_or_404
from django_htmx.http import retarget
from project.models import Product
from project.forms import ProductForm
from django.http import JsonResponse, HttpResponse
from django.db.models.query import QuerySet

def show_products(request):
    if request.htmx:
        products: QuerySet[Product] = Product.objects.all()
        context = {
            'products': products
        }
        return render(request, 'product/show_all.html', context)
    
def product_json(request):
    products: QuerySet[Product] = Product.objects.all()
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
        form: ProductForm = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            response = render(request, 'messages/product_sucess.html')
            return retarget(response, '#save_response')
        else:
            return HttpResponse({'success': False, 'errors': form.errors}, status=400)

def detail_product(request, id):
    if request.htmx:
        product: Product = get_object_or_404(Product, pk=id)
        context = {
            'product': product
        }
        response = render(request, 'product/details.html', context)
        return retarget(response, '.product')


    
    

        

        