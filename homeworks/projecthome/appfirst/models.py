from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


STATUSES = (
    ('M', 'главный судья'),
    ('J', 'судья'),
    ('S', 'секретарь'),
    ('O', 'наблюдатель'),
)


class Competition(models.Model):
    """Соревнования"""

    class Meta:
        db_table = 'competitions'

    name = models.CharField(max_length=50)
    fullname = models.CharField(max_length=150, default=None)
    date = models.DateField(default=None, null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class CompetitionTask(models.Model):
    """Задания в соревновании"""

    class Meta:
        db_table = 'competition_tasks'

    name = models.CharField(max_length=50)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class User(models.Model):
    class Meta:
        abstract = True  # данное поле указывает, что класс абстрактный
        # и что для него не нужно создавать таблицу

    name = models.CharField(_('Имя'), max_length=25)
    patronymic = models.CharField(_('Отчество'), max_length=25, default=None)
    last_name = models.CharField(_('Фамилия'), max_length=25)
    is_active = models.BooleanField(_('Удалить'), default=True)

    def __str__(self):
        return f"{self.last_name} {self.name}"


class Judge(User):
    class Meta:
        db_table = 'judges'

    post = models.CharField(_('Занимаемая должность'), max_length=100)
    regalia = models.TextField(_('Заслуги и регалии'), default=None)
    organization = models.CharField(_('Место работы'), max_length=100)
    status = models.CharField(_('Статус на соревнованиях'), max_length=1,
                              choices=STATUSES, default='O')
    competitions = models.ManyToManyField(Competition)

    def __str__(self):
        return f"{self.status}: {self.last_name} {self.name[0]}. {self.patronymic[0]}."
