from django.core.mail import send_mail

from menu.models import *

from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate


def sign_up(request):
    if request.method == 'GET':
        return render(request, 'accounts/sign_up.html', context={
            'title': 'Реєстрація'
        })
    elif request.method == 'POST':
        # 1 - Отримання даних із форми реєстрації:
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')
        pass2_x = request.POST.get('pass2')
        email_x = request.POST.get('email')

        # 2 - Валідація даних з боку сервера:
        color = 'gray'
        message = 'default'
        if pass1_x != pass2_x:
            color = 'red'
            message = 'Паролі не співпадають!'
        elif pass1_x == '':
            pass
        else:
            # 3 - Додавання користувача в базу даних:
            user = User.objects.create_user(login_x, email_x, pass1_x)

            # 4 - формування звіту:
            if user is None:
                color = 'red'
                message = 'В регістрації відмовлено!'
            else:
                user.save()
                color = 'green'
                message = 'Регістрацію успішно завершено'
        # 6 - Завантаження сторінки звіту:
        return render(request, 'home/index.html', context={
            'title': 'Звіт про реєстрацію',
            'color': color,
            'message': message
        })


def sign_in(request):
    if request.method == 'GET':
        return render(request, 'accounts/sign_in.html', context={
            'title': 'Авторизація'
        })
    elif request.method == 'POST':
        # 1 - Зчитаємо дані із форми:
        email_x = request.POST.get('email')
        pass_x = request.POST.get('pass')

        # 1.1. Получаем юзера
        user_x = get_user(email_x)
        if user_x is None:
            color = 'red'
            message = 'Користувач не знайдений або помилка в паролі!'
            return render(request, 'accounts/report.html', context={
                'color': color,
                'message': message
            })

        # 2 - Перевіряємо наявність запису у БД:
        user = authenticate(request, username=user_x, password=pass_x)
        if user is not None:
            login(request, user)
            return render(request, 'home/index.html')
        else:
            color = 'red'
            message = 'Користувач не знайдений або помилка в паролі!'
            return render(request, 'accounts/report.html', context={
                'color': color,
                'message': message
            })


def sign_out(request):
    logout(request)
    return render(request, 'home/index.html', context={
        'title': 'Вихід із системи'
    })


def profile(request):
    if request.method == 'GET':
        return render(request, 'accounts/profile.html', context={
            'title': 'Авторизація',
            'user_orders': Order.objects.filter(user_id=request.user.id)
        })
    else:
        return render(request, 'accounts/profile.html', context={
            'title': 'Профіль користувача'
        })


def ajax_email(request):
    email_y = request.GET.get('email')

    try:
        User.objects.get(email=email_y)
        message = 'зайнятий'
    except User.DoesNotExist:
        message = 'вільний'
    return JsonResponse({
        'message': message
    })


def get_user(email):
    user = User.objects.get(email=email)
    if user is None:
        return None
    else:
        return user


def cart(request):
    if request.method == 'GET':
        return render(request, 'accounts/cart.html', context={
            'title': 'Кошик',
            'user_orders': Order.objects.filter(user_id=request.user.id)
        })


def ajax_del_order_dynamics(request):
    response = dict()
    uid = request.GET['uid']
    user_orders = Order.objects.filter(user_id=uid)

    dict_products = list()
    for sp in user_orders:
        dict_products.append({
            "id": sp.id,
            "title": sp.title,
            "name": str(sp.product.name),
            "picture": str(sp.product.picture),
            "amount": sp.amount,
            "date": sp.date,
            "status": sp.status
        })

    response['orders'] = dict_products
    return JsonResponse(response)


def ajax_del_order(request):
    response = dict()
    order_id = request.GET['order_id']
    del_order = Order.objects.get(id=order_id)
    del_order.delete()
    response['message'] = f'AJAX - OJ / ID: {order_id}'
    return JsonResponse(response)


def confirm(request):
        if request.method == 'POST':
            labs = request.POST['labs']
            email = request.POST['email']
            adressa = request.POST['adressa']
            city = request.POST['city']
            state = request.POST['state']
            zip = request.POST['zip']

            order_info = Order.objects.filter(user_id=request.user.id)
            order_info_len = len(order_info)

            if order_info_len:
                subject = 'Оформлення підписки на сайті FastFood'
                body = """
                                <h4>Вітаємо!</h4>
                                <h4>Дякуємо Вам, за те що обрали наш чудовий ресторан!</h4>
                                <h4>Ваше замовленя успішно оплачено та вже прямує до Вас!</h4>
                                <h4>Номер вашого замовлення: 1465405641</h4>
                                
                                <br>
                                <h4>Даруємо Вам промокод на знижку 30% на купівлю однієї позиції з нашого ресторану!</h4>
                                <h4>Промокод: promo_3246234</h4>
                                <h4>Бажаєте використати свій бонус?:)</h4>
                                <div>
                                    <br>
                                    <a class="btn btn-success" href="http://127.0.0.1:8000/menu/">Перейти на сайт!</a>
                                </div>"""

                success = send_mail(subject, '', 'FastFood', [email], fail_silently=False, html_message=body)
                if success:
                    order_info.delete()
                    return  render(request, 'accounts/thanks.html', {
                        'labs': labs,
                        'email': email,
                        'adressa': adressa,
                        'city': city,
                        'state': state,
                        'zip': zip
                    })
                else:
                    return render(request, 'accounts/failed.html', {
                        'title': 'Помилка поштового відправлення'
                    })
            else:
                return render(request, 'accounts/failed.html', {
                    'title': 'Помилка поштового відправлення'
                })



