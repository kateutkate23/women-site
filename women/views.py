from django.http import HttpResponse
from django.shortcuts import render


# request = HttpRequest
def index(request):
    return HttpResponse('Main page of application.')


def categories(request, category_id):
    return HttpResponse(f'<h1>Category: {category_id}</h1>')


def categories_by_slug(request, category_slug):
    return HttpResponse(f'<h1>Category: {category_slug}</h1>')


def archive(request, year):
    return HttpResponse(f'<h1>Archive category from {year} year</h1>')
