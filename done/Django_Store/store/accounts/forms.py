from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        css = 'w-full border rounded px-3 py-2'
        self.fields['username'].widget.attrs.update({'class': css, 'placeholder': 'Имя пользователя'})
        self.fields['password1'].widget.attrs.update({'class': css, 'placeholder': 'Пароль'})
        self.fields['password2'].widget.attrs.update({'class': css, 'placeholder': 'Повтор пароля'})
