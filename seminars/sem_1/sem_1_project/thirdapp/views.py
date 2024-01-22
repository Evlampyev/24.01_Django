import logging
from http.client import HTTPResponse

from django.shortcuts import render
from random import choice, randint
from secondapp.models import Author, Post
from .forms import GamesChooseForm, AuthorAddForm, PostAddForm


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


def games_choose(request):
    if request.method == 'POST':
        form = GamesChooseForm(request.POST)
        if form.is_valid():
            game = form.cleaned_data['game']
            number = form.cleaned_data['number']
            if game == 'Орел или Решка':
                return heads_and_tails(request, number)
            elif game == 'Бросок кубика':
                return cube_faces(request, number)
            else:
                return random_digits(request, number)

    else:
        form = GamesChooseForm()
    return render(request, 'thirdapp/games_choose.html', {'form': form})


def add_author(request):
    if request.method == 'POST':
        form = AuthorAddForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            biography = form.cleaned_data['biography']
            birthday = form.cleaned_data['birthday']
            author = Author(name=name, last_name=last_name, email=email,
                            biography=biography, birthday=birthday)
            logging.info(f'Added author {last_name} {name}')
            author.save()
    else:
        form = AuthorAddForm()
    return render(request, 'thirdapp/add_author.html', {'form': form})


def add_post(request):
    if request.method == 'POST':
        form = PostAddForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            publish_date = form.cleaned_data['publish_date']
            author = form.cleaned_data['author']
            category = form.cleaned_data['category']
            views = form.cleaned_data['views']
            is_published = form.cleaned_data['is_published']
            post = Post(title=title, content=content, publish_date=publish_date, author=author,
                        category=category, views=views, is_published=is_published)
            post.save()
            logging.info(f'Пост {title} сохранена')
    else:
        form = PostAddForm()
    return render(request, 'thirdapp/add_post.html', {'form': form})
