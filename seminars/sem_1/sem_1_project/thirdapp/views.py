from http.client import HTTPResponse

from django.shortcuts import render
from random import choice, randint
from secondapp.models import Author, Post


# Create your views here.

def third_index(request):
    return render(request, 'thirdapp/index.html')


def heads_and_tails(request, count):
    lst = ['орел', 'решка']
    situations = []
    for i in range(count):
        situations.append(choice(lst))
    context = {'situations': situations, 'title': 'Орел и решка'}
    return render(request, 'thirdapp/games.html', context=context)


def cube_faces(request, count):
    result = []
    for i in range(count):
        result.append(randint(1, 7))
    context = {'cube_faces': result, 'title': 'Бросок кубика'}
    return render(request, 'thirdapp/games.html', context=context)


def random_digits(request, count):
    result = [randint(1, 100) for _ in range(count)]
    context = {'random_digits': result, 'title': 'Случайные числа'}
    return render(request, 'thirdapp/games.html', context=context)


def author_post(request, author_id):
    author = Author.objects.get(id=author_id)
    posts = Post.objects.filter(author=author)
    context = {'author': author, 'posts': posts}
    return render(request, 'thirdapp/author_post.html', context=context)


def post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'thirdapp/post.html', context={'post': post})
