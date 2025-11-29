from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect, render
from django.views import View

from task_manager.users.models import CustomUser

from .forms import SignUpForm, UserUpdateForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        return render(request, "users/index.html", context={"users": users, })


class UserFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'users/create.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Пользователь успешно зарегистрирован")
            return redirect('login')
        return render(request, 'users/create.html', {'form': form})


class UserCheckMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                request,
                "Вы не авторизованы! Пожалуйста, выполните вход."
            )
            return redirect('login')
        user_id = kwargs.get("id")
        if not request.user.id == user_id:
            messages.error(
                request,
                "У вас нет прав для изменения другого пользователя."
            )
            return redirect('users')
        return super().dispatch(request, *args, **kwargs)


class UserFormUpdateView(UserCheckMixin, View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get("id")
        user = CustomUser.objects.get(id=user_id)
        form = UserUpdateForm(instance=user)
        return render(
            request, "users/update.html", {"form": form, "user_id": user_id}
        )
    
    def post(self, request, *args, **kwargs):
        user_id = kwargs.get("id")
        user = CustomUser.objects.get(id=user_id)
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Пользователь успешно изменен")
            return redirect("users")
        return render(
            request, "users/update.html", {"form": form, "user_id": user_id}
        )


class UserFormDeleteView(UserCheckMixin, View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get("id")
        user = CustomUser.objects.get(id=user_id)
        if user:
            return render(
                request, "users/delete.html", {"user": user}
            )
    
    def post(self, request, *args, **kwargs):
        user_id = kwargs.get("id")
        user = CustomUser.objects.get(id=user_id)
        if user:
            try:
                user.delete()
                messages.success(request, "Пользователь успешно удален")
            except ProtectedError:
                messages.error(
                    request,
                    """Невозможно удалить пользователя, """
                    """потому что он используется"""
                )
        return redirect("users")