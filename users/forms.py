from django.contrib.auth.forms import UserCreationForm, \
    AuthenticationForm
from .models import User
from django import forms
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        help_text="Введіть ваш email"
    )

    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text="Пароль має бути не менш 8 символів і не повинен мати тільки цифри. Введіть якісь букви чи символи."
    )

    password2 = forms.CharField(
        label="Підтвердження пароля",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text="Введіть той-же самий пароль ще раз для підтвердження."
    )

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Паролі не співпадають.")

        return password2

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'autofocus': True})
    )



