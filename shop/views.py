from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    products = Product.objects.all()
    product_name=request.GET.get('product_name')

    #search code
    if product_name != '' and product_name is not None:
        products = products.filter(name__icontains=product_name)

    #paginator code
    paginator = Paginator(products,4)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    return render(request,'shop/index.html',{'products':products})

def detail(request,id):
    product = Product.objects.get(id=id)
    return render(request,'shop/detail.html',{'product':product})

def create_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()
            return redirect('shop:index')
    else:
        product_form = ProductForm()
    return render(request,'shop/create_form.html',{'product_form':product_form})

def edit_product(request,id):
    product = Product.objects.get(id=id)
    product_form = ProductForm(request.POST or None, instance=product)
    if product_form.is_valid():
        product_form.save()
        return redirect('shop:index')
    return render(request,'shop/create_form.html',{'product':product,'product_form':product_form})

def delete_product(request,id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('shop:index')
    return render(request,'shop/delete.html',{'product':product})