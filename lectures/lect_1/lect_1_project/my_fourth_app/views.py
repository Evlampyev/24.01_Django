import traceback

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from logging import getLogger
from .forms import UserForm, ManyFieldsForm, ManyFieldsFormWidget, ImageForm
from .models import User

# Create your views here.
logger = getLogger(__name__)


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = "Ошибка в данных"
        # создается не пустая форма, а на основе данных полученных от пользователя (request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # делаем что-то с данными
            # Например
            user = User(name=name, email=email, age=age)
            try:
                user.save()
                logger.info(f'Получили {name =}, {email =}, {age =}.')
                message = "Пользователь сохранен"
            except:
                form = UserForm(request.POST)
                message = "Такой email уже есть"


    else:
        form = UserForm()  # формируем пустую форму на основе класса UserForm
        message = 'Заполните форму'
    return render(request, 'my_fourth_app/user_form.html',
                  {'form': form, 'message': message})


def many_fields_form(request):
    if request.method == 'POST':
        # form = ManyFieldsForm(request.POST) #  будет форма на основе нового класса
        form = ManyFieldsFormWidget(request.POST)
        if form.is_valid():
            logger.info(f'Получили {form.cleaned_data=}.')
    else:
        form = ManyFieldsForm()
    return render(request, 'my_fourth_app/many_fields_form.html', {'form': form})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        # POST - нужен для сохранения текстовой информации,
        # Files - для получения файла

        if form.is_valid():
            image = form.cleaned_data['image'] # извлекаем изображение
            fs = FileSystemStorage() # экземпляр FileSystemStorage, позволяет работать с файлом
            fs.save(image.name, image) # сохранение файла
    else:
        form = ImageForm()
    return render(request, 'my_fourth_app/upload_image.html', {'form': form})


