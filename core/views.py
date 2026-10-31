from django.shortcuts import render
from product.models import Product


def home_view(requst):
    
    product = Product.objects.all()
    
    context = {
        'product': product
    }
    
    return render(requst, 'home.html',context)