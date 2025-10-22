from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views import View
from .forms import SignUpForm

from task_manager.users.models import CustomUser


class IndexView(View):
    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        return render(
            request,
            "users/index.html",
            context={
                "users": users,
            },
        )


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'users/create.html', {'form': form})


class UserFormUpdateView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get("id")
        user = CustomUser.objects.get(id=user_id)
        form = SignUpForm(instance=user)
        return render(
            request, "users/update.html", {"form": form, "user_id": user_id}
        )
    
    def post(self, request, *args, **kwargs):
        user_id = kwargs.get("id")
        user = CustomUser.objects.get(id=user_id)
        form = SignUpForm(request.POST, instance=auser)
        if form.is_valid():
            form.save()
            return redirect("users")
        return render(
            request, "users/update.html", {"form": form, "user_id": user_id}
        )