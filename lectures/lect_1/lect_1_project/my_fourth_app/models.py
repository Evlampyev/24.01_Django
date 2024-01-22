from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f'Имя: {self.name}, email: {self.email}, возраст: {self.age}.'
