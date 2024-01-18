from django.shortcuts import render
from django.http import HttpResponse
from random import choice, randint
from logging import getLogger
from .models import Money, Author, Post
from datetime import datetime
import json

# Create your views here.

logger = getLogger(__name__)


def heads_and_tails(request):
    logger.info("Орел и решка страница")
    lst = ['орел', 'решка']
    situation = choice(lst)
    time = datetime.now()
    money = Money(situation=situation, time_created=time)
    money.save()
    return HttpResponse(situation)


def ht_results(request):
    result = Money.get_data(5)

    return HttpResponse(str(result))


def cube_faces(request):
    logger.info("Случайное число от 1 до 6")
    return HttpResponse(randint(1, 6))


def random_digits(request):
    logger.info("Случайное число от 1 до 100")
    return HttpResponse(randint(1, 100))


def authors_view(request):
    authors = Author.objects.all()
    res_str = '<br>'.join([str(author) for author in authors])
    return HttpResponse(str(res_str))


def posts_view(request):
    posts = Post.objects.all()
    res_str = '<br>'.join([str(post) for post in posts])
    return HttpResponse(res_str)


def index_view(request):
    context = {'name': 'Alexander'}
    return render(request, 'secondapp/index.html', context)