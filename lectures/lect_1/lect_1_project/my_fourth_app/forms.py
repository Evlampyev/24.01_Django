import datetime

from django import forms


class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=0, max_value=120)

    def clean_name(self):
        """Проверка на заглавную букву"""
        name = self.cleaned_data['name']
        if name != name.title():
            raise forms.ValidationError("Имя должно быть с заглавной буквы")
        return name

    def clean_email(self):
        """Проверка на использование корпоративной почты"""
        email: str = self.cleaned_data['email']
        if not (email.endswith('vk.team') or email.endswith('1pku.ru')):
            raise forms.ValidationError("Используйте корпоративную почту")
        return email


class ManyFieldsForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=18)
    height = forms.FloatField()
    is_active = forms.BooleanField(required=False)
    birthdate = forms.DateField(
        initial=datetime.date.today())  # по умолчанию текущая дата
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])


class ManyFieldsFormWidget(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите имя пользователя'}))
    # сюда же мы прописываем классы стилей для полей
    # 'placeholder': 'Введите имя пользователя' - серая надпись в поле
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'user@mail.ru'}))
    age = forms.IntegerField(min_value=18,
                             widget=forms.NumberInput(attrs={'class': 'form-control'}))
    height = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    is_active = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'form-check-input'}))
    birthdate = forms.DateField(initial=datetime.date.today,
                                widget=forms.DateInput(attrs={
                                    'class': 'form-control',
                                    'type' : 'date'  # теперь календарь
                                }))
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')],
                               widget=forms.RadioSelect(
                                   attrs={'class': 'form-check-input'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


class ImageForm(forms.Form):
    image = forms.ImageField()
