from django.shortcuts import render
from store.models import Product

def home(request):
    products = Product.objects.filter(is_available=True)[:4]

    context = {
        'title': 'Home',
        'products' : products,
        }
        
    return render(request, "home.html", context)