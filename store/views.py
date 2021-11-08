from django.shortcuts import render
from django.utils.text import slugify
from category.models import Category
from store.models import Product

# Create your views here.
def store(request, category_slug=None):
    if category_slug:
        cat = Category.objects.get(slug=category_slug)
        products = Product.objects.filter(category=cat, is_available=True)
    else:
        products = Product.objects.all()
    
    products_count = products.count()
    context = {
        'title' : 'Tienda',
        'products' : products,
        'products_count' : products_count,
    }
    return render(request, 'store.html', context)


def product_detail(request, category_slug, product_slug):
    product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    context = {
        'title' : 'detalle',
        'product' : product,
    }
    return render(request, 'product_detail.html', context)