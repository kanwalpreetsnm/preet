from django.shortcuts import render
from .models import Category, product
# Create your views here.

def category(request):
    categories=Category.objects.all()
    context={'categories':categories}
    return render(request,'shop/index.html',context)

def products(request,slug):
    category=Category.objects.filter(slug=slug).first()
    products=product.objects.filter(Category=category)
    context={'products':products}
    return render(request,'shop/products.html',context)

def productdetail(request,slug):
    oneproduct=product.objects.filter(slug=slug).first()
    context={'oneproduct':oneproduct}
    return render(request,'shop/productdetail.html',context)
    


