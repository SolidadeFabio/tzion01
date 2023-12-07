from django.shortcuts import render
from project.models import Product

def show_product(request):
    if request.htmx:
        products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request, 'product/show.html', context)
    
def create_product(request):
    if request.htmx:
        return render(request, 'product/create.html')

        

        