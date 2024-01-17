from django.core.management.base import BaseCommand
from my_second_app.models import User


class Command(BaseCommand):
    help = 'Create a new user'

    def handle(self, *args, **kwargs):
        # user = User(name='John', email='john@example.com', password='secret', age=25)
        # user = User(name='Neo', email='neo@example.com', password='secret', age=58)
        user = User(name='Jack', email='capitan@example.com', password='secret', age=60)

        user.save()
        self.stdout.write(f'Created new user: {user}')



