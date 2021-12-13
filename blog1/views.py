from django.shortcuts import render
from blog1.models import Category
from blog1.models import POST


# Create your views here.

def home(request):
    posts=POST.objects.all()
    category=Category.objects.all()
    context={'posts':posts,'category':category}
    return render(request,'blog1/home.html',context)

def postcategory(request,slug):
    category=Category.objects.filter(slug=slug).first()
    posts=POST.objects.filter(category=category)
    context={'post':posts}
    return render(request,'blog1/postcategories.html', context)
    
def postdetail(request,slug):
    post=POST.objects.filter(slug=slug).first()
    context={'posts':post}
    return render(request,'blog1/postdetails.html', context)

    
    
    
