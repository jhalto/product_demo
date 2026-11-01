from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

from product.models import Product
from .forms import ProductForm
def product_detail(request, id):
    
    product  = get_object_or_404(Product, id = id)
    
    return render(request, 'product_detail.html',  context= {
        'product': product
    })

@login_required    
def product_edit(request, id):
    
    product = get_object_or_404(Product, id = id)
    
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance= product)
        
        if form.is_valid:
            form.save()
            return redirect('home_view')
            
    else:
        form = ProductForm(instance= product)
    
    context = {
        'form': form
    } 
    return render(request, 'product_edit.html', context)
@login_required
@permission_required(perm=['product.add_product'], raise_exception= True)
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('home_view')
    else:
        form = ProductForm()
        
    context = {
        'form': form
    }
    return render(request,'product_add.html', context)
@permission_required(perm=['product.delete_product'], raise_exception= True)
def product_delete(request, id):
    product = get_object_or_404(Product, id = id)
    
    if request.method == "POST":
        product.delete()
        return redirect('home_view')
    return redirect('home_view')