
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('accounts/',include('allauth.urls')),
    path('orders/',include('order.urls',namespace='orders')),
    path('cart/',include('cart.urls',namespace='cart')),
    path('payment/',include('payment.urls',namespace='payment')),
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,Document_root=settings.MEDIA_ROOT)