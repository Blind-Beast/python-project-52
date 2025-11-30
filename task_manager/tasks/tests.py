import pytest
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.urls import reverse

from task_manager.statuses.models import Status

from .models import Task

User = get_user_model()


@pytest.mark.django_db
class TestTaskCRUD:
    def setup_method(self):
        self.user1 = User.objects.create_user(
            username='first_user',
            password='pass12word'
        )
        self.user2 = User.objects.create_user(
            username='second_user',
            password='pass34word'
        )
        self.status = Status.objects.create(name='Статус')

    def test_create_task(self, client):
        client.login(username='first_user', password='pass12word')
        url = reverse('tasks_create')
        data = {
            'name': 'Тестовая задача',
            'description': 'Описание задачи',
            'status': self.status.id,
            'executor': self.user2.id
        }
        response = client.post(url, data)
        assert response.status_code == 302
        assert Task.objects.count() == 1
        assert Task.objects.first().author == self.user1

    def test_update_task(self, client):
        task = Task.objects.create(
            name='Тестовая задача', status=self.status,
            author=self.user1
        )
        client.login(username='first_user', password='pass12word')
        url = reverse('tasks_update', kwargs={'id': task.id})
        response = client.post(url, {
            'name': 'Обновленная задача',
            'description': 'Обновоенное описание',
            'status': self.status.id
        })
        assert response.status_code == 302
        task.refresh_from_db()
        assert task.name == 'Обновленная задача'

    def test_delete_task_by_author(self, client):
        task = Task.objects.create(
            name='Тестовая задача',
            status=self.status,
            author=self.user1
        )
        client.login(username='first_user', password='pass12word')
        url = reverse('tasks_delete', kwargs={'id': task.id})
        response = client.post(url)
        assert response.status_code == 302
        assert Task.objects.count() == 0

    def test_delete_task_by_non_author(self, client):
        task = Task.objects.create(
            name='Тестовая задача',
            status=self.status,
            author=self.user1
        )
        client.login(username='second_user', password='pass34word')
        url = reverse('tasks_delete', kwargs={'id': task.id})
        response = client.post(url)
        assert Task.objects.count() == 1
        messages = list(get_messages(response.wsgi_request))
        assert "только ее автор" in str(messages[0])


