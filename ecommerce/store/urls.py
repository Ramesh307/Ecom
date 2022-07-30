from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from . import views

app_name = 'store'

urlpatterns = [
	#Leave as empty string for base url

	path('',views.store,name="store_view"),
	path('/filter/<int:category_id>',views.product_filter_category,name='product_filterc'),
	path('/product_detail/<int:product_id>',views.product_detail,name="product_detail")
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)