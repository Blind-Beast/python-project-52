from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
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
            messages.success(request, _('User created successfully'))
            return redirect('login')
        return render(request, 'users/create.html', {'form': form})


class UserCheckMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                request,
                _("You are not logged in! Please log in.")
            )
            return redirect('login')
        user_id = kwargs.get("id")
        if not request.user.id == user_id:
            messages.error(
                request,
                _("You do not have permission to perform this action.")
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
            messages.success(request, _('User updated successfully'))
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
                messages.success(request, _('User deleted successfully'))
            except ProtectedError:
                messages.error(
                    request,
                    _("It is impossible to delete the user \
                    because it is being used")
                )
        return redirect("users")