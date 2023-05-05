from django.shortcuts import render, get_object_or_404
from . models import Category, Product

# Create your views here.

def index(request):
    return render(request, 'index.html')


def store(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products' : products})

def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'product_detail.html', {'product' : product})
    
    