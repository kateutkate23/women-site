from django.http import HttpResponse
from django.shortcuts import render


# request = HttpRequest
def index(request):
    return HttpResponse('Main page of application.')


def categories(request):
    return HttpResponse('<h1>Categories</h1>')
