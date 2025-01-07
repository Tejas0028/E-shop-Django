from django.shortcuts import render,get_object_or_404
from .models import Product
from category.models import Category
# Create your views here.

def store(request,category_slug=None):
    categories = None
    products = None
    category_list = Category.objects.all()

    if category_slug != None:
        categories = get_object_or_404(Category,slug = category_slug)
        products = Product.objects.filter(category = categories,is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {
        "products": products,
        "product_count": product_count,
        "category_list":category_list,
    }

    return render(request,'store/store.html',context)


def product_detail(request,category_slug,product_slug):
    single_product = get_object_or_404(Product,category__slug = category_slug,slug=product_slug)
    
    context = {
        "single_product":single_product,
    }
    return render(request,'store/detail.html',context)