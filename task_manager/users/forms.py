from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import CustomUser


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=150,
        required=True,
        label=_("First name"),
        label_suffix='',
        widget=forms.TextInput(
            attrs={'placeholder': _("First name"), 'class': 'form-control', }
        )
    )
    last_name = forms.CharField(
        max_length=150,
        required=True,
        label=_("Last name"),
        label_suffix='',
        widget=forms.TextInput(
            attrs={'placeholder': _("Last name"), 'class': 'form-control', }
        )
    )
    username = forms.CharField(
        max_length=150,
        required=True,
        label=_("Username"),
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'placeholder': _("Username"),
                'class': 'form-control',
                'aria-describedby': "id_username_helptext",
            }
        )
    )
    password1 = forms.CharField(
        max_length=150,
        required=True,
        label=_("Password"),
        label_suffix='',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': _("Password"),
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
        label=_("Confirm Password"),
        label_suffix='',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': _("Confirm Password"),
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
        label=_("Username"),
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'placeholder': _("Username"),
                'class': 'form-control',
                'autocomplete': "username",
            }
        )
    )
    password = forms.CharField(
        required=True,
        label=_("Password"),
        label_suffix='',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': _("Password"),
                'class': 'form-control',
                'autocomplete': "current-password",
            }
        )
    )


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=150,
        required=True,
        label=_("First name"),
        label_suffix='',
        widget=forms.TextInput(
            attrs={'placeholder': _("First name"), 'class': 'form-control', }
        )
    )
    last_name = forms.CharField(
        max_length=150,
        required=True,
        label=_("Last name"),
        label_suffix='',
        widget=forms.TextInput(
            attrs={'placeholder': _("Last name"), 'class': 'form-control', }
        )
    )
    username = forms.CharField(
        max_length=150,
        required=True,
        label=_("Username"),
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'placeholder': _("Username"),
                'class': 'form-control',
                'aria-describedby': "id_username_helptext",
            }
        )
    )
    password1 = forms.CharField(
        max_length=150,
        required=True,
        label=_("Password"),
        label_suffix='',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': _("Password"),
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
        label=_("Confirm Password"),
        label_suffix='',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': _("Confirm Password"),
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