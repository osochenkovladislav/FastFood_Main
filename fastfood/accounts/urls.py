from django.urls import path
from .views import *


urlpatterns = [
    path('sign_up', sign_up),
    path('sign_in', sign_in),
    path('sign_out', sign_out),
    path('profile', profile),
    path('confirm', confirm),
    path('ajax_email', ajax_email),
    path('cart', cart),
    path('ajax_del_order_dynamics', ajax_del_order_dynamics),
    path('ajax_del_order', ajax_del_order),
]