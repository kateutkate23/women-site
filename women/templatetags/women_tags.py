from django import template
import women.views as views

register = template.Library()


@register.simple_tag()
def get_categories():
    return views.categories_db


@register.inclusion_tag('women/list_categories.html')
def show_categories(selected_category=0):
    categories = views.categories_db
    return {'categories': categories, 'selected_category': selected_category}