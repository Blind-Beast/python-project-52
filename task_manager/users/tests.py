import pytest
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse

from task_manager.statuses.models import Status
from task_manager.tasks.models import Task

User = get_user_model()


@pytest.mark.django_db
class UserCRUDTests(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.user1 = User.objects.get(pk=1)  # admin
        self.user2 = User.objects.get(pk=2)  # JohnDoe
        self.user3 = User.objects.get(pk=3)  # User

        for user in [self.user1, self.user2, self.user3]:
            user.set_password('pass12word')
            user.save()

    def test_user_registration(self):
        initial_users = User.objects.count()

        url = reverse('users_create')
        data = {
            'username': 'newuser',
            'password1': 'pass34word',
            'password2': 'pass34word',
            'first_name': 'New',
            'last_name': 'User'
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), initial_users + 1)
        self.assertTrue(User.objects.filter(username='newuser').exists())

        messages = list(get_messages(response.wsgi_request))
        assert "успешно" in str(messages[0]).lower()

    def test_user_update_authenticated(self):
        self.client.login(username='JohnDoe', password='pass12word')
        url = reverse('users_update', kwargs={'id': self.user2.pk})
        response = self.client.post(
            url,
            {
                'username': 'JohnDoe',
                'first_name': 'Updated',
                'last_name': 'User',
                'password1': 'pass12word',
                'password2': 'pass12word',
            }
        )
        self.assertRedirects(response, reverse('users'))
        self.user2.refresh_from_db()
        self.assertEqual(self.user2.first_name, 'Updated')
        self.assertTrue(self.user2.check_password('pass12word'))

    def test_cannot_delete_user_with_tasks(self):
        status = Status.objects.create(name='Статус')

        Task.objects.create(
            name="Тестовая задача",
            status=status,
            author=self.user1
        )

        self.client.login(username='JohnDoe', password='pass34word')
        self.client.post(reverse('users_delete', args=[self.user1.id]))

        self.assertTrue(User.objects.filter(id=self.user1.id).exists())