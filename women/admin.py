from django.contrib import admin
from django.core.checks import messages
from django.utils.safestring import mark_safe

from .models import Women, Category


class MarriedFilter(admin.SimpleListFilter):
    title = 'Статус женщины'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Замужем'),
            ('single', 'Не замужем')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(husband__isnull=True)


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'post_photo', 'created_at', 'is_published', 'category')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    list_per_page = 10
    list_filter = (MarriedFilter, 'category__name', 'is_published')
    ordering = ('created_at', 'title')
    actions = ('publish', 'unpublish')
    search_fields = ('title', 'category__name')

    fields = ('title', 'slug', 'content', 'photo', 'category', 'husband', 'tags')
    prepopulated_fields = {"slug": ("title",)}

    filter_horizontal = ('tags',)

    @admin.display(description='Изображение')
    def post_photo(self, women: Women):
        if women.photo:
            return mark_safe(f"<img src='{women.photo.url}' width=50>")
        return "Без фото"

    @admin.action(description='Опубликовать выбранные записи')
    def publish(self, request, queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f"Было опубликовано записей: {count}")

    @admin.action(description="Снять с публикации выбранные записи")
    def unpublish(self, request, queryset):
        count = queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(request, f"Снято с публикации записей: {count}!", messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
