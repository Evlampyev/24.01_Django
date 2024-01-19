from django.db import models


# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'Title is {self.title}.'



    def get_summary(self):
        """Возвращает начало новости из 12 слов"""
        words = self.content.split()
        return f'{" ".join(words[:12])}...'
