from django import forms
import datetime
from secondapp.models import Author, Post


class GamesChooseForm(forms.Form):
    CHOICES = [
        ('M', 'Орел или Решка'),
        ('C', 'Бросок кубика'),
        ('N', 'Случайное число')
    ]
    game = forms.ChoiceField(choices=CHOICES)
    number = forms.IntegerField(min_value=1, max_value=64)


# class AuthorAddForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     biography = forms.CharField()
#     birthday = forms.DateField(initial=datetime.date.today,
#                                widget=forms.DateInput(attrs={
#                                    'class': 'form-control',
#                                    'type' : 'date'  # теперь календарь
#                                }))

class AuthorAddForm(forms.ModelForm):
    """Тоже самое, что и выше, только облегченный вариант"""

    class Meta:
        model = Author
        fields = ['name', 'last_name', 'email', 'biography', 'birthday']


class PostAddForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'views', 'is_published']

    publish_date = forms.DateField(initial=datetime.date.today,
                                   widget=forms.DateInput(attrs={
                                       'class': 'form-control',
                                       'type' : 'date'  # теперь календарь
                                   }))
    author = forms.ModelChoiceField(queryset=Author.objects.all().order_by('last_name'))
