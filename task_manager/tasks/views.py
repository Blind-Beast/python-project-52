from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext_lazy as _
from django.views import View

from task_manager.tasks.models import Task

from .filters import TaskFilter
from .forms import TaskForm


class IndexView(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        tasks_filter = TaskFilter(request.GET, queryset=tasks, request=request)
        tasks = tasks_filter.qs
        return render(
            request,
            "tasks/index.html",
            context={"tasks": tasks, "filter": tasks_filter, })


class TaskView(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs["id"])
        return render(request, "tasks/show.html", context={"task": task, })


class TaskFormCreateView(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, "tasks/create.html", {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            form.save_m2m()
            messages.success(request, _("Task successfully created"))
            return redirect('tasks')
        return render(request, 'tasks/create.html', {'form': form})


class TaskFormUpdateView(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request, *args, **kwargs):
        task_id = kwargs.get("id")
        task = Task.objects.get(id=task_id)
        form = TaskForm(instance=task)
        return render(
            request, "tasks/update.html", {"form": form, "task_id": task_id}
        )
    
    def post(self, request, *args, **kwargs):
        task_id = kwargs.get("id")
        task = Task.objects.get(id=task_id)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, _("Task successfully updated"))
            return redirect("tasks")
        return render(
            request, "tasks/update.html", {"form": form, "task_id": task_id}
        )


class TaskFormDeleteView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get("id")
        task = Task.objects.get(id=task_id)
        if not task.author.id == request.user.id:
            messages.error(request, _("Only the author can delete an issue."))
            return redirect('tasks')
        if task:
            return render(
                request, "tasks/delete.html", {"task": task}
            )
    
    def post(self, request, *args, **kwargs):
        task_id = kwargs.get("id")
        task = Task.objects.get(id=task_id)
        if not task.author.id == request.user.id:
            messages.error(request, _("Only the author can delete an issue."))
            return redirect('tasks')
        if task:
            task.delete()
        messages.success(request, _("Task successfully deleted"))
        return redirect("tasks")