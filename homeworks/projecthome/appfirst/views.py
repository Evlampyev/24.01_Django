from django.http import HttpResponse
from django.shortcuts import render, redirect
from pathlib import Path
from logging import getLogger
from appfirst.models import Judge, Competition
from .form import UserForm

# Create your views here.

logger = getLogger(__name__)


def index(request):
    context = {'info': ['Всем привет!', 'И добро пожаловать!']}
    logger.info('Главная страница')
    return render(request, 'appfirst/index.html', context=context)


def edit_judges(request):
    judges = Judge.objects.all()

    # list_result = [judge for judge in temp]
    context = {
        'title' : ["№ п\п", 'Имя', "Отчество", "Фамилия", "Должность", "Заслуги",
                   "Место работы", "Статус", 'Соревнование', "Редактор"],
        'judges': judges
    }
    return render(request, 'appfirst/edit_judges.html', context=context)


# def edit_judges(request):
#     list_competition = Judge.competition.through.objects.all().values_list()
#     competition = [comp for comp in list_competition]
#     comp_dict = {}  # словарь: judge_id:[comp_id]
#     for comp in competition:
#         if comp[1] in comp_dict:
#             comp_dict[comp[1]].append(comp[2])
#         else:
#             comp_dict[comp[1]] = [comp[2]]
#     print(comp_dict)
#     # temp = Judge.objects.all().values()
#     temp = Judge.objects.filter(status='J').values()
#     list_result = []
#     for judge in temp:
#         # print(judge)
#         judge['comp'] = " ".join(
#             Competition.objects.filter(pk=comp_dict[judge['id']][0]).values_list('name',
#                                                                                  flat=True))
#         # print(judge)
#         # если в списке (comp_dict) у судьи несколько соревнований, то не работает,
#         # нужно из списка строку с разделителем сделать
#         # print(comp_dict)
#         list_result.append(judge)
#     # list_result = [judge for judge in temp]
#     context = {
#         'title' : ["№ п\п", 'Имя', "Отчество", "Фамилия", "Должность", "Заслуги",
#                    "Место работы", "Статус", 'Соревнование', "Редактор"],
#         'judges': list_result
#     }
#     return render(request, 'appfirst/edit_judges.html', context=context)


def delete_judge(request, pk):
    """Delete judge on pk"""
    judge = Judge.objects.filter(id=pk)
    judge.delete()
    logger.info(f'{judge} deleted')
    return redirect('/first/edit_judges/')


def edit_judge(request):
    pass


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
            judge = Judge(name=name, patronymic=patronymic, last_name=last_name,
                          organization=organization, post=post, regalia=regalia,
                          status=status, is_active=is_active)
            # разобраться с соревнованиеми
            judge.save()
            logger.info(f'Получили данные {name=}, {last_name=}.')
            return redirect('/first/edit_judges/')

    else:
        form = UserForm()
    return render(request, 'appfirst/add_judge.html', {'form': form})


def edit_competitions(request):
    list_competition = Competition.objects.all().values()
    temp = [comp for comp in list_competition]
    comp_dict = {'competitions': temp}
    comp_dict['title'] = ['№ п/п', 'Краткое название', "Полное наименование", "Сроки",
                          "Активен", "Редактор"]
    print(temp)
    return render(request, 'appfirst/edit_competitions.html', context=comp_dict)


def base(request):
    logger.info('Базовый шаблон. Зачем сюда-то?')
    return render(request, 'base.html')


def about(request):
    logger.info("Загружена страница обо мне")
    html = ("<p>Эта страница про меня<br>и мой первый сайт</p>"
            "<a href='{% url 'index' %}'>на главную</a>")
    return HttpResponse(html)
