from shop.models import Category
from django.http import request
from django.shortcuts import render,redirect,get_object_or_404
from .models import Category, Product

# Create your views here.
def product_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = Category.objects.all()
        products = products.objects.filter(slug=category_slug)


    context = {
        'category': category,
        'categories':categories,
        'Product':products,
    }

    return render(request,'index.html',context)


def product_detail(request,id,slug):
    product = get_object_or_404(slug=slug,id=id)
