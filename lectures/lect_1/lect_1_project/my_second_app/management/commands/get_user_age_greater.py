from django.core.management.base import BaseCommand
from my_second_app.models import User


class Command(BaseCommand):
    help = "Get user with age greater <age>."

    def add_arguments(self, parser):
        """Добавление ключевого аргумента в handle по ключу 'age'"""
        parser.add_argument('age', type=int, help='User age')

    def handle(self, *args, **kwargs):
        age = kwargs['age']  # Извлечение возраста из ключевых аргументов по ключу
        user = User.objects.filter(age__gt=age)
        self.stdout.write(f'{user}')
