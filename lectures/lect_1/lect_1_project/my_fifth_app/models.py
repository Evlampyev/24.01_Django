from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = _('Категории')  # Название таблицы в админ-панели

    name = models.CharField(_('Название'), max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = _('Продукты')

    name = models.CharField(_('Наименование'), max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # если удалим категорию, то удалятся все продукты
    description = models.TextField(_('Описание'), default='', blank=True)
    # blank=True -поле обязательное для заполнения
    price = models.DecimalField(_('Цена'), default=999999.99, max_digits=8,
                                decimal_places=2)
    quantity = models.PositiveSmallIntegerField(_('Количество'), default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    # поле заполняется автоматически, текущее время
    rating = models.DecimalField(_('Рейтинг'), default=5.0, max_digits=3,
                                 decimal_places=2)

    def __str__(self):
        return self.name
