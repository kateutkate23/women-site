from django.contrib import admin
from .models import Women, Category


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'is_published', 'category')
    list_display_links = ('id', 'title')
    list_editable = ('is_published', )
    list_per_page = 10
    ordering = ('created_at', 'title')


# admin.site.register(Women, WomenAdmin)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
