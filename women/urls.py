from django.urls import path, register_converter

from . import views, converters

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index),
    path('categories/<int:category_id>/', views.categories),
    path('categories/<slug:category_slug>/', views.categories_by_slug),
    path('archive/<year4:year>/', views.archive),
]
