from django.http import HttpResponse
from django.shortcuts import render
from pathlib import Path
from logging import getLogger
from appfirst.models import Judge

# Create your views here.

logger = getLogger(__name__)


def index(request):
    context = {'info': ['Всем привет!', 'И добро пожаловать!']}
    logger.info('Главная страница')
    return render(request, 'appfirst/index.html', context=context)


def edit_judges(request):
    # temp = Judge.objects.filter(status='j')
    temp = Judge.objects.all().values()
    list_result = [judge for judge in temp]
    context = {
        'title' : ["№ п\п", 'Имя', "Отчество", "Фамилия", "Должность", "Заслуги",
                   "Место работы", "Статус", 'Соревнование'],
        'judges': list_result
    }
    return render(request, 'appfirst/edit_judges.html', context=context)


def base(request):
    logger.info('Базовый шаблон. Зачем сюда-то?')
    return render(request, 'base.html')


def about(request):
    logger.info("Загружена страница обо мне")
    html = ("<p>Эта страница про меня<br>и мой первый сайт</p>"
            "<a href='index'>на главную</a>")
    return HttpResponse(html)
