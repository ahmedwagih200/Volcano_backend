from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products.views import *
from adminpanel.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.social.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('category/<id>', get_product),
    path('categories', get_category),
    path('cate/<id>', get_cate),
    path('review/', include('customer.urls')),
    path('feedback/', include('feedback.urls')),
    path('cate/<id>', get_cate),
    path('order', create_order),
    path('orders/<id>', get_orders),
    path('order/<id>', get_order),
    path('adminpanel', home),
    path('admin-cate', admin_cate),
    path('admin-prod', admin_prod),
    path('admin-order', admin_order),
    path('admin-user', admin_user),
    path('del-cate<id>', del_cate),
    path('get_product_payment/<id>', get_product_payment),
    path('api/stripe/', include('visa.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
