from datetime import datetime

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'float': 3.14,
        'lst': [1, 2, 3, 'adf', True],
        'set': {1, 2, 2, 3, 4, 4, 5},
        'dct': {'k1': 'v1', 'k2': 'v2'},
        'obj': MyClass(10, 20)
    }
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})


def categories(request, category_id):
    return HttpResponse(f'<h1>Category: {category_id}</h1>')


def categories_by_slug(request, category_slug):
    return HttpResponse(f'<h1>Category: {category_slug}</h1>')


def archive(request, year):
    if year > datetime.now().year:
        redirect_url = reverse('categories', args=('music',))
        return redirect(redirect_url)

    return HttpResponse(f'<h1>Archive category from {year} year</h1>')


def page_not_found(request, exception):
    return HttpResponseNotFound(f'<h1>Page not found</h1>')
