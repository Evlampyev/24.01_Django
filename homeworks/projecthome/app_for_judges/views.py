from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from pathlib import Path
from logging import getLogger
from .forms import UserForm, CompetitionForm
from appfirst.models import Judge, Competition
from django.contrib import messages

# Create your views here.


logger = getLogger(__name__)

JUDGE_TABLE_TITLE = ["№ п\п", 'Имя', "Отчество", "Фамилия", "Должность", "Заслуги",
                     "Место работы", "Статус", 'Соревнование', "Редактор"]


def index(request):
    context = {'info': ['Всем привет!', 'И добро пожаловать!']}
    logger.info('Главная страница')
    return render(request, 'judges/index.html', context=context)


def edit_judges(request):
    # judges = Judge.objects.all()
    judges = Judge.objects.filter(is_active=True).order_by('last_name')
    competitions_dict = {}
    for judge in judges:
        competitions_dict[judge.pk] = [comp for comp in
                                       judge.competitions.all().values_list('name',
                                                                            flat=True)]
    context = {
        'title'       : JUDGE_TABLE_TITLE,
        'judges'      : judges,
        'competitions': competitions_dict
    }
    return render(request, 'judges/edit_judges.html', context=context)


def delete_judge(request, pk):
    """Delete judge on pk"""
    judge = Judge.objects.get(id=pk)
    print(f" For delete {judge = }")
    # judge.delete()
    logger.info(f'{judge} deleted')
    judge.is_active = False
    judge.save()
    messages.success(request, "Пользователь удален")
    return redirect('/first/edit_judges/')


def add_judge(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name'].capitalize()
            patronymic = form.cleaned_data['patronymic'].capitalize()
            last_name = form.cleaned_data['last_name'].capitalize()
            post = form.cleaned_data['post'].capitalize()
            regalia = form.cleaned_data['regalia']
            organization = form.cleaned_data['organization']
            status = form.cleaned_data['status']
            competition = form.cleaned_data['competition']
            # is_active = form.cleaned_data['is_active']
            # comp = Competition.objects.filter(name=competition)
            judge = Judge(name=name, patronymic=patronymic, last_name=last_name,
                          organization=organization, post=post, regalia=regalia,
                          status=status)
            judge.save()
            if competition:
                competition.judge_set.add(judge)
            # добавляет в поле со связью многие ко многим
            logger.info(f'Получили данные {"name"} {last_name}.')

            messages.success(request, 'Судья добавлен')
            return redirect('/first/edit_judges/')

    else:
        form = UserForm()
    return render(request, 'judges/edit_judge.html', {'form': form})


def edit_judge(request, pk):
    judge = get_object_or_404(Judge, id=pk)

    if request.method == 'GET':
        context = {'form': UserForm(instance=judge), 'id': pk}
        return render(request, 'judges/edit_judge.html', context)

    elif request.method == 'POST':
        form = UserForm(request.POST, instance=judge)
        if form.is_valid():
            temp_date = form.cleaned_data['date']
            print(temp_date)
            form.save()
            messages.success(request, 'Изменения сохранены')
            return redirect('edit_judges')
        else:
            messages.error(request, 'Пожалуйста, исправьте следующие ошибки:')
            return render(request, 'judges/edit_judge.html', {'form': form})


def base(request):
    logger.info('Базовый шаблон. Зачем сюда-то?')
    return render(request, 'base.html')


def about(request):
    logger.info("Загружена страница обо мне")
    html = ("<p>Эта страница про меня<br>и мой первый сайт</p>"
            "<a href='{% url 'index' %}'>на главную</a>")
    return HttpResponse(html)