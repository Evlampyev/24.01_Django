from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from pathlib import Path
from logging import getLogger
from .forms import UserForm
from appfirst.models import Judge, Competition
from django.contrib import messages

# Create your views here.


logger = getLogger(__name__)

JUDGE_TABLE_TITLE = ["№ п\п", 'Имя', "Отчество", "Фамилия", "Должность", "Заслуги",
                     "Место работы", "Статус", 'Соревнование', "Редактор"]

COMPETITIONS_TABLE_TITLE = ['№ п/п', 'Краткое название', "Полное наименование", "Сроки",
                            "Активен", "Редактор"]


def index(request):
    context = {'info': ['Всем привет!', 'И добро пожаловать!']}
    logger.info('Главная страница')
    return render(request, 'appfirst/index.html', context=context)


def edit_judges(request):
    # judges = Judge.objects.all()
    judges = Judge.objects.filter(is_active=True).order_by('last_name')
    competitions_dict = {}
    for judge in judges:
        competitions_dict[judge.pk] = [comp for comp in
                                       judge.competitions.all().values_list('name',
                                                                            flat=True)]
    print(f'{competitions_dict=}')

    context = {
        'title'       : JUDGE_TABLE_TITLE,
        'judges'      : judges,
        'competitions': competitions_dict
    }
    return render(request, 'appfirst/edit_judges.html', context=context)


def delete_judge(request, pk):
    """Delete judge on pk"""
    judge = Judge.objects.get(id=pk)
    print(f" For delete {judge = }")
    # judge.delete()
    logger.info(f'{judge} deleted')
    judge.is_active = False
    judge.save()
    return redirect('/first/edit_judges/')


def add_judge(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            patronymic = form.cleaned_data['patronymic']
            last_name = form.cleaned_data['last_name']
            post = form.cleaned_data['post']
            regalia = form.cleaned_data['regalia']
            organization = form.cleaned_data['organization']
            status = form.cleaned_data['status']
            competition = form.cleaned_data['competition']
            is_active = form.cleaned_data['is_active']
            comp = Competition.objects.filter(name=competition)
            judge = Judge(name=name, patronymic=patronymic, last_name=last_name,
                          organization=organization, post=post, regalia=regalia,
                          status=status, is_active=is_active)
            judge.save()
            competition.judge_set.add(judge)
            # добавляет в поле со связью многие ко многим
            logger.info(f'Получили данные {"name"} {last_name}.')

            messages.success(request, 'Судья добавлен')
            return redirect('/first/edit_judges/')

    else:
        form = UserForm()
    return render(request, 'appfirst/edit_judge.html', {'form': form})


def edit_competitions(request):
    competitions = Competition.objects.all().order_by('name')
    # temp = [comp for comp in list_competition]
    context = dict()
    context['competitions'] = competitions
    context['title'] = COMPETITIONS_TABLE_TITLE
    print(competitions)
    return render(request, 'appfirst/edit_competitions.html', context=context)


def add_competition(request):
    return HttpResponse('Добавить')


def base(request):
    logger.info('Базовый шаблон. Зачем сюда-то?')
    return render(request, 'base.html')


def about(request):
    logger.info("Загружена страница обо мне")
    html = ("<p>Эта страница про меня<br>и мой первый сайт</p>"
            "<a href='{% url 'index' %}'>на главную</a>")
    return HttpResponse(html)


def edit_judge(request, pk):
    judge = get_object_or_404(Judge, id=pk)

    if request.method == 'GET':
        context = {'form': UserForm(instance=judge), 'id': pk}
        return render(request, 'appfirst/edit_judge.html', context)
    elif request.method == 'POST':
        form = UserForm(request.POST, instance=judge)
        if form.is_valid():
            form.save()
            messages.success(request, 'Изменения сохранены')
            return redirect('edit_judges')
        else:
            messages.error(request, 'Пожалуйста, исправьте следующие ошибки:')
            return render(request, 'appfirst/edit_judge.html', {'form': form})
