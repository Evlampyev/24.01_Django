from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render  # для передачи данных в шаблон
from django.views.generic import \
    TemplateView  # класс который может создавать представля на основе класса с особенностями


# Create your views here.


def hello(request):
    return HttpResponse('Hello World from function!')


class HelloWorld(View):
    @staticmethod
    def get(request):
        return HttpResponse('Hello World from class')


def year_post(request, year):
    text = ''
    # формируем статьи за год
    return HttpResponse(f"Posts from {year}<br>{text}")


class MonthPost(View):
    def get(self, request, year, month):
        text = ''
        # формируем статьи за год и месяц
        return HttpResponse(f"post from {month}/{year}<br>{text}")


def post_detail(request, year, month, slug):
    """Формируем статьи за год и месяц по идентификатору."""
    # Пока обойдёмся без запросов к базе данных
    post = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "Кто быстрее создаёт списки в Python, list() или []",
        "content": "В процессе написания очередной программы задумался над тем, "
                   "какой способ создания списков в Python работает быстрее..."}
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})
    # возвращаем не http объект, а json объект
    # json_dumps_params={'ensure_ascii': False} - говорит о том, что могут быть любые символы,
    # а не только латиница (ascii)


def my_view(request):
    # request - запрос, приходит от пользователя
    data = {'name': 'Alex'}
    return render(request, 'my_third_app/template_from_app.html', context=data)


class TemplIf(TemplateView):
    template_name = "my_third_app/templ_if.html"  # зарезервированное имя

    def get_context_data(self, **kwargs):  # kwargs - распаковка словаря
        context = super().get_context_data(**kwargs)  # извлечение контекста который пришел свыше
        context['message'] = 'Привет из TemlateView!'
        context['number'] = 5
        return context


def view_for(request):
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
        'каждый': 'красный',
        'охотник': 'оранжевый',
        'желает': 'жёлтый',
        'знать': 'зелёный',
        'где': 'голубой',
        'сидит': 'синий',
        'фазан': 'фиолетовый',
    }
    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'my_third_app/templ_for.html', context)
