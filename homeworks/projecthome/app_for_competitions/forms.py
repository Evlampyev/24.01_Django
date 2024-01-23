from django import forms
import datetime
from .models import Competition
from django.utils.translation import gettext_lazy as _


class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition

        fields = ['name', 'fullname']

    date = forms.DateField(label=_("Дата"), initial=datetime.date.today,
                           widget=forms.DateInput(attrs={
                               'class': 'form-control',
                               'type' : 'date'  # теперь календарь
                           }))
    active = forms.BooleanField(label=_("Активно"), required=False, widget=forms.CheckboxInput(
        attrs={'class': 'form-check-input'}))
