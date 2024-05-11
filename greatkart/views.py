# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Home Page Ezoa")

from django.shortcuts import render 
from store.models import Product
#send something from web

def home(request):
    products=Product.objects.all().filter(is_available=True)
    #add the product value inside the context
    context={
        'products':products,
    }
    
    return render(request,'home.html',context)
