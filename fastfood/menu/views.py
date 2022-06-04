from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import *
from .forms import ProductForm, ProductFormUpdate
import json


def index(request):
    return render(request, 'menu/menu.html', context={
        'title': 'Меню',
        'burger_obj': Product.objects.filter(category=1),
        'sneks_obj': Product.objects.filter(category=3),
        'desert_obj': Product.objects.filter(category=4),
        'drink_obj': Product.objects.filter(category=2)
    })


def create(request):
    data = dict()
    data['title'] = 'Додавання товару'
    if request.method == 'GET':
        if request.user.username == 'admin123':
            data['form'] = ProductForm()
            return render(request, 'menu/create.html', data)
        else:
            logout(request)
            return redirect('/accounts/sing_in')
    elif request.method == 'POST':
        filled_form = ProductForm(request.POST, request.FILES)
        filled_form.save()
        return redirect('/menu')


def update(request, product_id: int):
    data = dict()
    data['title'] = 'Редагування товару'
    product = Product.objects.get(id=product_id)
    if request.method == 'GET':
        if request.user.username == 'admin123':
            data['form'] = ProductFormUpdate(instance=product)
            data['product'] = product
            return render(request, 'menu/update.html', data)
        else:
            logout(request)
            return redirect('/accounts/sing_in')
    elif request.method == 'POST':
        filled_form = ProductFormUpdate(request.POST, request.FILES)
        print(filled_form.errors.as_data())
        if filled_form.is_valid():
            product.name = filled_form.cleaned_data['name']
            product.about = filled_form.cleaned_data['about']
            product.category = filled_form.cleaned_data['category']
            product.price = filled_form.cleaned_data['price']
            product.save()
        return redirect('/menu')


def delete(request, product_id: int):
    data = dict()
    data['title'] = 'Видалення товару'
    product = Product.objects.get(id=product_id)
    if request.method == 'GET':
        if request.user.username == 'admin123':
            data['product'] = product
            return render(request, 'menu/delete.html', data)
        else:
            logout(request)
            return redirect('/menu/sing_in')
    elif request.method == 'POST':
        product.delete()
        return redirect('/menu')


def ajax_cart(request):
    response = dict()
    uid = request.GET.get('uid')
    pid = request.GET.get('pid')
    price = request.GET.get('price')
    response['uid'] = f'UID: {uid}'
    response['pid'] = f'PID: {pid}'
    response['price'] = f'PRICE: {price}'
    product = Product.objects.get(id=pid)
    Order.objects.create(
        title=f'Order-{pid}/{uid}',
        amount=float(product.price),
        status='очікування підтвердження',
        product_id=pid,
        user_id=uid
    )
    user_orders = Order.objects.filter(user_id=uid)
    amount = 0
    for order in user_orders:
        amount += order.amount
    response['amount'] = amount
    response['count'] = len(user_orders)
    return JsonResponse(response)


def ajax_cart_display(request):
    response = dict()
    uid = request.GET['uid']
    user_orders = Order.objects.filter(user_id=uid)
    s = 0
    for order in user_orders:
        s += order.amount
    response['amount'] = s
    response['count'] = len(user_orders)
    return JsonResponse(response)




