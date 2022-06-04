from django.urls import re_path
from .views import *

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    re_path(r'^price/$', price_api),
    re_path(r'^price/([0-9]+)$', price_api),
    re_path(r'^order/$', order_api),
    re_path(r'^order/([0-9]+)$', order_api),
    re_path(r'^product/$', product_api),
    re_path(r'^product/([0-9]+)$', product_api),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)