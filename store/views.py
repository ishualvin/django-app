from django.shortcuts import render, get_object_or_404
from . models import Category, Product
from django.contrib import messages

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
    if request.method == "POST":
        first_name = request.POST.get('first_name','')
        last_name = request.POST.get('last_name','')
        email =	request.POST.get('email','')
        subject = request.POST.get('subject','')
        message = request.POST.get('message','')
        if len(first_name)<2 or len(email)<3 or len(subject)<10 or len(message)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, desc=desc)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, 'contact.html')

def thankyou(request):
    return render(request, 'thankyou.html')

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'product_detail.html', {'product' : product})
    
    