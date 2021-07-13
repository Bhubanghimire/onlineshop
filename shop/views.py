from shop.models import Category
from django.http import request
from django.shortcuts import render,get_object_or_404
from .models import Category, Product

# Create your views here.
def product_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    products= Product.objects.filter(available=True)
    print(category_slug)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    
    context = {
        'category': category,
        'categories':categories,
        'products':products,
    }
    # print(products)
    return render(request,'shop/product/list.html',context)


def product_detail(request,id,slug):
    product = get_object_or_404(Product, slug=slug,id=id,available=True)

    return render(request,'shop/product/detail.html',{'product':product})
