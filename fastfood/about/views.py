from django.shortcuts import render


def index(request):
    return render(request, 'about/about.html', context={
        'title': 'Про компанію'
    })
