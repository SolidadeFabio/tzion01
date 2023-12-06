from django.shortcuts import render

def product_home(request):
    
    if request.htmx:
        return render(request, 'product.html')
    else:
        print("Deu ruim :(")
        

        