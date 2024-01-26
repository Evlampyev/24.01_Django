"""Настройка внешнего вида и функциональности админ панели"""

from django.contrib import admin
from .models import Category, Product


# Register your models here.

@admin.action(description='Сбросить количество в ноль')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    """Список продуктов"""
    list_display = ['name', 'category', 'quantity']
    ordering = ['category', '-quantity']
    # указание на автоматическую сортировку в админ панели в той последовательности, как указано
    list_filter = ['date_added', 'price']
    search_fields = ['description']  # добавление поля поиска
    search_help_text = ['Поиск по полю описание продукта']  # подсказка к поиску
    actions = [reset_quantity]  # функцию указываем по названию без кавычек

    """Отдельный продукт"""
    # fields = ['name', 'description', 'category', 'date_added', 'rating']
    readonly_fields = ['date_added', 'rating']

    fieldsets = [  # можно использовать только fieldsets или fields
        (
            None,
            {
                'classes': ['wide'],
                # класс "wide", что означает, что она будет занимать все доступное место на странице
                'fields' : ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes'    : ['collapse'],  # будут скрыты по умолчанию (класс "collapse"),
                'description': 'Категория товара и его подробное описание',
                'fields'     : ['category', 'description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Рейтинг и прочее',
            {
                'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
                'fields'     : ['rating', 'date_added'],
            }
        ),
    ]


admin.site.register(Category)  # Добавили в админ панель модель Category
admin.site.register(Product, ProductAdmin)
