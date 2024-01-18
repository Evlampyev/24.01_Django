from django.core.management.base import BaseCommand
from secondapp.models import Author
from typing import Any
from datetime import date


class Command(BaseCommand):
    help = " Creats new users"

    def handle(self, *args: Any, **kwargs: Any) -> str | None:
        for i in range(1, 11):
            author = Author(
                name=f'Author{i}',
                last_name=f'Last_name{i}',
                email=f'Email{i}@mail.ru',
                biography=f'Lorem ipsum dolor sit amet',
                birthday=date.today())
            author.save()
        return self.stdout.write(f'Created new ten users')
