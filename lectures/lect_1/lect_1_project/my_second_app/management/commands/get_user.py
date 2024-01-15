from django.core.management.base import BaseCommand
from my_second_app.models import User


class Command(BaseCommand):
    help = "Get user by id."

    def add_arguments(self, parser):
        # pk = primary_kay
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        user = User.objects.filter(pk=pk).first()
        self.stdout.write(f'{user}')
