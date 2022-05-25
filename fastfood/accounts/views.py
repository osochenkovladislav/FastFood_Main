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
            message = 'Користувач не знайдений'
            title = 'Звіт про авторизацію'
            return render(request, 'accounts/report.html', context={
                'color': color,
                'message': message,
                'title': title
            })

        # 2 - Перевіряємо наявність запису у БД:
        user = authenticate(request, username=user_x, password=pass_x)
        if user is not None:
            login(request, user)
            return render(request, 'home/index.html')
        else:
            color = 'red'
            message = 'Користувач не знайдений'
            title = 'Звіт про авторизацію'
            return render(request, 'accounts/report.html', context={
                'color': color,
                'message': message,
                'title': title
            })


def sign_out(request):
    logout(request)
    return render(request, 'home/index.html', context={
        'title': 'Вихід із системи'
    })


def profile(request):
    return render(request, 'home/index.html', context={
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

