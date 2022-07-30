from math import prod
from django.shortcuts import render, redirect , get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Product
from cart.carts import Carts
from .forms import CartAddProductForm

@require_POST
def cart_add(request, product_id):
    cart = Carts(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,quantity=cd['quantity'],override_quantity=cd['override'])
    return redirect('cart:cart_detail')

def cart_add_main(request,product_id):
    cart = Carts(request)
    product = get_object_or_404(Product,id=product_id)
    cart.add(product=product,quantity=1)
    return redirect('store:store_view')

@require_POST
def cart_remove(request, product_id):
    cart = Carts(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Carts(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity':item['quantity'],
            'override': True
        })
    return render(request, 'cart/detail.html',{'cart':cart})
