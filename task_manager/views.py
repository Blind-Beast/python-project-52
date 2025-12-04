from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _

from .users.forms import LoginForm


def index(request):
    return render(request, "index.html",)


def login_view(request):
    form = LoginForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, _("You are logged in"))
                return redirect('/')
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, _("You are logged out"))
    return redirect('/')