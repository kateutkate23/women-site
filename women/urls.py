from django.urls import path, register_converter

from . import views, converters

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('categories/<int:category_id>/', views.categories, name='categories_by_id'),
    path('categories/<slug:category_slug>/', views.categories_by_slug, name='categories'),
    path('archive/<year4:year>/', views.archive, name='archive'),
]
