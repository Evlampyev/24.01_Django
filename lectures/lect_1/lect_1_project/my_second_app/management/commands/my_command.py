from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Print 'Hello world!' to output"  # отображается как справка

    def handle(self, *args, **kwargs):
        self.stdout.write('Hello world!')
