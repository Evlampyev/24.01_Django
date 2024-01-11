from django.shortcuts import render
from django.http import HttpResponse
from random import choice, randint
from logging import getLogger

# Create your views here.

logger = getLogger(__name__)


def heads_and_tails(request):
    logger.info("Орел и решка страница")
    lst = ['орел', 'решка']

    return HttpResponse(choice(lst))


def cube_faces(request):
    logger.info("Случайное число от 1 до 6")
    return HttpResponse(randint(1, 6))


def random_digits(request):
    logger.info("Случайное число от 1 до 100")
    return HttpResponse(randint(1, 100))
