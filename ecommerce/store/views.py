
from django.shortcuts import render,get_object_or_404
from .models import *
from cart.forms import CartAddProductForm
from .recommender import Recommender



# def store(request):
# 	category = None
#     categories = Category.objects.all()
#     products = Product.objects.filter(available = True)
#     if category_slug:
#         category = get_object_or_404(Category,slug = category_slug)
#         products = products.filter(category=category)
#     return render(request,'shop/product/list.html',{'category':category,'categories':categories,'products':products})

def main(request):
    category= Category.objects.all()
    return render(request,'store/Main.html',{'category':category})

def product_filter_category(request,category_id):
    category = get_object_or_404(Category,id=category_id)
    products = Product.objects.filter(category=category)
    return render(request,'store/store_filter.html',{'products':products})

def store(request):
    products = Product.objects.all()
    return render(request,'store/store.html',{'products':products})
    



def product_detail(request,product_id):
    product = get_object_or_404(Product,id=product_id)
    cart_product_form = CartAddProductForm()
    r=Recommender()
    recommended_products=r.suggest_products_for([product],4)
    form = cart_product_form
    return render(request,'store/product_detail.html',{'product':product,'cart_product_form':cart_product_form,'recommended_products':recommended_products})