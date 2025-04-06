from datetime import datetime

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse


# request = HttpRequest
def index(request):
    return HttpResponse('Main page of application.')


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
