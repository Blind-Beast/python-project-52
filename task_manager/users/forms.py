from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import CustomUser


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=150,
        required=True,
        label="Имя",
        label_suffix='',
        widget=forms.TextInput(
            attrs={'placeholder': 'Имя', 'class': 'form-control', }
        )
    )
    last_name = forms.CharField(
        max_length=150,
        required=True,
        label="Фамилия",
        label_suffix='',
        widget=forms.TextInput(
            attrs={'placeholder': 'Фамилия', 'class': 'form-control', }
        )
    )
    username = forms.CharField(
        max_length=150,
        required=True,
        label="Имя пользователя",
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Имя пользователя',
                'class': 'form-control',
                'aria-describedby': "id_username_helptext",
            }
        )
    )
    password1 = forms.CharField(
        max_length=150,
        required=True,
        label="Пароль",
        label_suffix='',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Пароль',
                'class': 'form-control',
                'autocomplete': "new-password",
                'id': 'id_password1',
                'aria-describedby': "id_password1_helptext",
            }
        )
    )
    password2 = forms.CharField(
        max_length=150,
        required=True,
        label="Подтверждение пароля",
        label_suffix='',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Подтверждение пароля',
                'class': 'form-control',
                'autocomplete': "new-password",
                'id': 'id_password2',
                'aria-describedby': "id_password2_helptext",
            }
        )
    )
    
    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2'
        )


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        label="Имя пользователя",
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Имя пользователя',
                'class': 'form-control',
                'autocomplete': "username",
            }
        )
    )
    password = forms.CharField(
        required=True,
        label="Пароль",
        label_suffix='',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Пароль',
                'class': 'form-control',
                'autocomplete': "current-password",
            }
        )
    )


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=150,
        required=True,
        label="Имя",
        label_suffix='',
        widget=forms.TextInput(
            attrs={'placeholder': 'Имя', 'class': 'form-control', }
        )
    )
    last_name = forms.CharField(
        max_length=150,
        required=True,
        label="Фамилия",
        label_suffix='',
        widget=forms.TextInput(
            attrs={'placeholder': 'Фамилия', 'class': 'form-control', }
        )
    )
    username = forms.CharField(
        max_length=150,
        required=True,
        label="Имя пользователя",
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Имя пользователя',
                'class': 'form-control',
                'aria-describedby': "id_username_helptext",
            }
        )
    )
    password1 = forms.CharField(
        max_length=150,
        required=True,
        label="Пароль",
        label_suffix='',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Пароль',
                'class': 'form-control',
                'autocomplete': "new-password",
                'id': 'id_password1',
                'aria-describedby': "id_password1_helptext",
            }
        )
    )
    password2 = forms.CharField(
        max_length=150,
        required=True,
        label="Подтверждение пароля",
        label_suffix='',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Подтверждение пароля',
                'class': 'form-control',
                'autocomplete': "new-password",
                'id': 'id_password2',
                'aria-describedby': "id_password2_helptext",
            }
        )
    )
    
    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2'
        )