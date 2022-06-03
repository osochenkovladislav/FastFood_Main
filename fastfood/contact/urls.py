from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('write_review', write_review),
]
