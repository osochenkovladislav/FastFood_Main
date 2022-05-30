from django.shortcuts import render
from .models import *

def index(request):

    return render(request, 'menu/index.html', context={
        'title': 'Меню',
        'burger_obj': Product.objects.filter(category=1),
        'sneks_obj': Product.objects.filter(category=3),
        'desert_obj': Product.objects.filter(category=4),
        'drink_obj': Product.objects.filter(category=2)
    })

