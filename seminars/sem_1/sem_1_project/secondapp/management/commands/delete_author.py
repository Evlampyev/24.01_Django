from django.core.management.base import BaseCommand
from secondapp.models import Author


class Command(BaseCommand):
    help = 'Delete uthor by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Id of the user to delete')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        author = Author.objects.filter(pk=pk).first()
        author.delete()
        self.stdout.write(f'{author.last_name} deleted')
