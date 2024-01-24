from django.contrib import admin
from .models import Category, Product

# Register your models here.

admin.site.register(Category) # Добавили в админ панель модель Category
admin.site.register(Product)

