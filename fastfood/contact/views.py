from django.shortcuts import render
from .models import Comment


def index(request):
    return render(request, 'contact/index.html', context={
        'title': 'Contact',
        'all_comments': Comment.objects.all()
    })


def write_review(request):
    if request.method == 'GET':
        return render(request, 'contact/index.html', context={
            'title': 'Відгуки'
        })
    elif request.method == 'POST':
        if request.user.is_authenticated == True:
            review = request.POST['text']

            Comment.objects.create(
                user=request.user,
                comment=review
            )

            return render(request, 'contact/wrire_review.html', context={
                'title': 'Дякуємо!',
                'all_comments': Comment.objects.all()
            })

