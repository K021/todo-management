from datetime import datetime
from django import forms
from django.utils import timezone

from todo.models import Todo


class TodoForm(forms.Form):
    CHOICES = (
        (1, '아주 중요'),
        (2, '중요'),
        (3, '보통'),
        (4, '별로 안 중요'),
    )

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        )
    )
    expiration = forms.DateTimeField(
        required=False,
        label='마감기한',
        initial=timezone.make_aware(datetime.now()),
        widget=forms.DateTimeInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    priority = forms.ChoiceField(
        label='우선순위',
        initial=(3, '보통'),
        choices=CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )

    def save(self, commit=True):
        todo = Todo(**self.cleaned_data)
        if commit:
            todo.save()
        return todo





















