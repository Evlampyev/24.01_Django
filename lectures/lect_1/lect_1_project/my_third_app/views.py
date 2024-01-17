from django.http import HttpResponse, JsonResponse
from django.views import View


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
