from django.shortcuts import render
from django.core.mail import send_mail


def index(request):
    return render(request, 'home/index.html', context={
        'title': 'Головна'
    })


def menu(request):
    return render(request, 'menu/menu.html', context={
        'title': 'Menu'
    })


def subscribe(request):
    if request.method == 'GET':
        return render(request, 'home/subscribe.html', context={
            'title': 'Підписатися'
        })
    elif request.method == 'POST':
        email = request.POST['email']
        #
        subject = 'Повідомлення про підписку на сайті Burgers'
        body = """
            <hr/>
            <h1>Дякуємо за підписку на сайті Burgers</h1>
            <hr/>
        """
        #
        success = send_mail(subject, '', 'FastFood', [email], fail_silently=False, html_message=body)
        if success:
            return render(request, 'home/subscribe.html', {
                'title': 'Дяка за замовлення',
                'email': email
            })
        else:
            return render(request, 'home/failed.html', {
                'title': 'Помилка пошового відправлення'
            })
