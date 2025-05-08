from django import template
from django.db.models import Count

from women.models import Category, TagPost

register = template.Library()


@register.inclusion_tag('women/list_categories.html')
def show_categories(selected_category=0):
    categories = Category.objects.annotate(total=Count('posts')).filter(total__gt=0)
    return {'categories': categories, 'selected_category': selected_category}


@register.inclusion_tag('women/list_tags.html')
def show_all_tags():
    return {'tags': TagPost.objects.annotate(total=Count('posts')).filter(total__gt=0)}
