from django import forms
from .models import Competition, STATUSES, Judge


class UserForm(forms.ModelForm):
    class Meta:
        model = Judge

        fields = ['name', 'patronymic', 'last_name', 'post', 'regalia', 'organization']

    # name = forms.CharField(max_length=25)
    # patronymic = forms.CharField(empty_value="")
    # last_name = forms.CharField(max_length=25)
    # post = forms.CharField(max_length=100)
    # regalia = forms.CharField(empty_value="")
    # organization = forms.CharField(max_length=100)
    status = forms.ChoiceField(choices=STATUSES)
    competition = forms.ModelChoiceField(
        queryset=Competition.objects.all().order_by('name'))
    is_active = forms.BooleanField(required=True)  # по умолчанию галочка на True
