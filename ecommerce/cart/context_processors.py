from .carts import Carts
from store.models import Category

def cart(request):
    return {'cart':Carts(request)}

def category(request):
    return {'category':Category.objects.all()}