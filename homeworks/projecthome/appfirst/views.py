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
    return render(request, 'appfirst/edit_judge.html', {'form': form})


def edit_judge(request, pk):
    judge = get_object_or_404(Judge, id=pk)

    if request.method == 'GET':
        context = {'form': UserForm(instance=judge), 'id': pk}
        return render(request, 'appfirst/edit_judge.html', context)

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
            return render(request, 'appfirst/edit_judge.html', {'form': form})


def edit_competitions(request):
    competitions = Competition.objects.all().order_by('name')
    context = dict()
    print(competitions[0])
    print(f"{competitions[0].date = }")

    for comp in competitions:
        print(comp.date)
    context['competitions'] = competitions
    context['title'] = COMPETITIONS_TABLE_TITLE
    return render(request, 'appfirst/edit_competitions.html', context=context)


def add_competition(request):
    if request.method == 'POST':
        form = CompetitionForm(request.POST)
        if form.is_valid():
            # form.save()
            name = form.cleaned_data['name']
            full_name = form.cleaned_data['fullname']
            date = form.cleaned_data['date']
            active = form.cleaned_data['active']
            comp = Competition(name=name, fullname=full_name, date=date, active=active)
            comp.save()
            # logger.info(f'Добавили {form.cleaned_data["name"]}')
            logger.info(f'Добавили конкурс: {name}')
            messages.success(request, "Конкурс добавлен")
            return redirect('/first/edit_competitions/')
    else:
        form = CompetitionForm()
    return render(request, 'appfirst/edit_competition.html', {'form': form})


def competition_activate(request, pk):
    competition = Competition.objects.filter(id=pk).first()
    competition.active = not competition.active
    competition.save()
    messages.success(request, "Статус соревнования изменён")
    return redirect('edit_competitions')


def delete_competition(request, pk):
    competition = Competition.objects.filter(id=pk)
    name = competition[0]
    competition.delete()
    logger.info(f"Соревнование {name} удалено")
    messages.success(request, f"Соревнование {name} удалено")
    return redirect('edit_competitions')


def edit_competition(request, pk):
    competition = get_object_or_404(Competition, id=pk)

    if request.method == 'GET':
        context = {'form': CompetitionForm(instance=competition), 'id': pk}
        return render(request, 'appfirst/edit_competition.html', context)

    elif request.method == 'POST':
        form = CompetitionForm(request.POST, instance=competition)
        if form.is_valid():
            competition.name = form.cleaned_data['name']
            competition.fullname = form.cleaned_data['fullname']
            competition.date = form.cleaned_data['date']
            competition.active = form.cleaned_data['active']
            competition.save()
            messages.success(request, f"Изменения сохранены")
            return redirect('edit_competitions')
        else:
            messages.error(request, 'Пожалуйста, исправьте следующие ошибки:')
            return render(request, 'appfirst/edit_competition.html', {'form': form})


def base(request):
    logger.info('Базовый шаблон. Зачем сюда-то?')
    return render(request, 'base.html')


def about(request):
    logger.info("Загружена страница обо мне")
    html = ("<p>Эта страница про меня<br>и мой первый сайт</p>"
            "<a href='{% url 'index' %}'>на главную</a>")
    return HttpResponse(html)
