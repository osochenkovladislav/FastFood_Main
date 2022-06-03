from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', index),
    path('create', create),
    path('ajax_cart', ajax_cart),
    path('ajax_cart_display', ajax_cart_display),
    re_path(r'^update/(?P<product_id>[0-9]+)$', update),
    re_path(r'^delete/(?P<product_id>[0-9]+)$', delete)
]