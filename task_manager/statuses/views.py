from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError
from django.views import View
from .forms import StatusForm

from task_manager.statuses.models import Status

class IndexView(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request, *args, **kwargs):
        statuses = Status.objects.all()
        return render(request, "statuses/index.html", context={"statuses": statuses,})

class StatusFormCreateView(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request, *args, **kwargs):
        form = StatusForm()
        return render(request, "statuses/create.html", {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Статус успешно создан")
            return redirect('statuses')
        return render(request, 'statuses/create.html', {'form': form})

class StatusFormUpdateView(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request, *args, **kwargs):
        status_id = kwargs.get("id")
        status = Status.objects.get(id=status_id)
        form = StatusForm(instance=status)
        return render(
            request, "statuses/update.html", {"form": form, "status_id": status_id}
        )
    
    def post(self, request, *args, **kwargs):
        status_id = kwargs.get("id")
        status = Status.objects.get(id=status_id)
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            messages.success(request, "Статус успешно изменен")
            return redirect("statuses")
        return render(
            request, "statuses/update.html", {"form": form, "status_id": status_id}
        )

class StatusFormDeleteView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        status_id = kwargs.get("id")
        status = Status.objects.get(id=status_id)
        if status:
            return render(
                request, "statuses/delete.html", {"status": status}
            )
    
    def post(self, request, *args, **kwargs):
        try:
            status_id = kwargs.get("id")
            status = Status.objects.get(id=status_id)
            if status:
                status.delete()
            messages.success(request, "Статус успешно удален")
            return redirect("statuses")
        except ProtectedError:
            messages.error(
                request,
                "Невозможно удалить статус, потому что он используется"
            )
            return redirect('statuses')