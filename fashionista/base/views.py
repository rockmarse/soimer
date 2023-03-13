from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    categories = products.objects.all()
    certificates_content=certificates.objects.all()
    
    services_content=services.objects.all()
    
    context = {'categories': categories,'certificates_content':certificates_content,'services_content':services_content}

    return render(request,'base/home.html',context)

# def viewmore(request,slug):
    
#     productsEl = products.objects.get(category=slug)
#     context = { 'detail':productsEl}
#     return render(request,"base/viewmore.html",context )

# def Products(request):
#     Products = products.objects.all()
#     context={'Products':Products}
#     return render(request,'base/products.html',context)


def viewmore(request, category):
    products_in_category = products.objects.filter(category=category)
    context = {'products': products_in_category, 'category': category}
    return render(request, 'base/viewmore.html', context)


def services_details(request,slug):
    
    productsEl = services.objects.get(service_heading = slug)
    
    context = { 'detail':productsEl}
    return render(request,"base/shipping.html",context )



def whybeele(request):
    whywe_content=whywe.objects.all()

    context={'whywe_content':whywe_content}

    return render(request,'base/whybeele.html',context)
def shipping(request):
    shipping_world=shipping.objects.all()

    context={'shipping_world':shipping_world}

    return render(request,'base/shipping.html',context)
def contact(request):

    return render(request,'base/contact.html')
def support(request):

    return render(request,'base/support.html')

