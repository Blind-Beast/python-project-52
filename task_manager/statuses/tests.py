import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

from task_manager.tasks.models import Task

from .models import Status

User = get_user_model()


@pytest.mark.django_db
class TestStatusCRUD:
    @pytest.fixture
    def logged_client(self, client):
        User.objects.create_user(username='first_user', password='pass12word')
        client.login(username='first_user', password='pass12word')
        return client

    def test_create_status(self, logged_client):
        url = reverse('statuses_create')
        response = logged_client.post(url, {'name': 'Тестовый статус'})
        assert response.status_code == 302
        assert Status.objects.filter(name='Тестовый статус').exists()

    def test_update_status(self, logged_client):
        status = Status.objects.create(name='Тестовый статус')
        url = reverse('statuses_update', args=[status.pk])
        logged_client.post(url, {'name': 'Новый статус'})
        status.refresh_from_db()
        assert status.name == 'Новый статус'

    def test_delete_status(self, logged_client):
        status = Status.objects.create(name='Удалить')
        url = reverse('statuses_delete', args=[status.pk])
        logged_client.post(url)
        assert not Status.objects.filter(pk=status.pk).exists()

    def test_status_list_requires_login(self, client):
        url = reverse('statuses')
        response = client.get(url)
        assert response.status_code == 302

    def test_cannot_delete_status_in_use(self, logged_client):
        status = Status.objects.create(name='Статус')
        author = User.objects.get(username='first_user')
        Task.objects.create(
            name='Тестовая задача',
            status=status,
            author=author
        )

        url = reverse('statuses_delete', args=[status.pk])
        response = logged_client.post(url)

        assert response.status_code == 302

        assert Status.objects.filter(pk=status.pk).exists()




