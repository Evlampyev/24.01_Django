from django.core.management.base import BaseCommand
from secondapp.models import Post, Author
from typing import Any
from datetime import date


class Command(BaseCommand):
    help = " Creates new posts"

    def add_arguments(self, parser) -> None:
        parser.add_argument('count', type=int, default=5,
                            help='Number of posts to create per author')

    def handle(self, *args: Any, **kwargs: Any):
        count = kwargs.get('count')
        authors = Author.objects.all()
        for author in authors:
            for i in range(count):
                post = Post(
                    title=f'Title{i}',
                    content=f'Content{i}',
                    author=author,
                    category='Comedy'
                )
                post.save()
        return self.stdout.write(f'Created new ten posts per author')
