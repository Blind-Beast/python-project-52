from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View

from task_manager.labels.models import Label

from .forms import LabelForm


class IndexView(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request, *args, **kwargs):
        labels = Label.objects.all()
        return render(
            request,
            "labels/index.html",
            context={"labels": labels, }
        )


class LabelFormCreateView(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request, *args, **kwargs):
        form = LabelForm()
        return render(request, "labels/create.html", {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = LabelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Метка успешно создана")
            return redirect('labels')
        return render(request, 'labels/create.html', {'form': form})


class LabelFormUpdateView(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request, *args, **kwargs):
        label_id = kwargs.get("id")
        label = Label.objects.get(id=label_id)
        form = LabelForm(instance=label)
        return render(
            request, "labels/update.html", {"form": form, "label_id": label_id}
        )
    
    def post(self, request, *args, **kwargs):
        label_id = kwargs.get("id")
        label = Label.objects.get(id=label_id)
        form = LabelForm(request.POST, instance=label)
        if form.is_valid():
            form.save()
            messages.success(request, "Метка успешно изменена")
            return redirect("labels")
        return render(
            request, "labels/update.html", {"form": form, "label_id": label_id}
        )


class LabelFormDeleteView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        label_id = kwargs.get("id")
        label = Label.objects.get(id=label_id)
        if label:
            return render(
                request, "labels/delete.html", {"label": label}
            )
    
    def post(self, request, *args, **kwargs):
        label_id = kwargs.get("id")
        label = Label.objects.get(id=label_id)
        if label.tasks.exists():
            messages.error(
                request,
                "Невозможно удалить метку, потому что она используется"
            )
            return redirect("labels")
        if label:
            label.delete()
        messages.success(request, "Метка успешно удалена")
        return redirect("labels")
        
        
            
