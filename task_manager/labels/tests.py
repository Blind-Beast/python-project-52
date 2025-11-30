
import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

# from django.test import TestCase
from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task

# class LabelsTest(TestCase):

#     def setUp(self):
#         self.label = Label.objects.create(name="Test label")
    
#     def test_label_created(self):
#         label = Label.objects.filter(name="Test label")
#         self.assertTrue(label.exists())

User = get_user_model()


@pytest.mark.django_db
class TestLabelViews:

    @pytest.fixture
    def user(self):
        return User.objects.create_user(
            username='testuser', password='pass12word'
            )

    @pytest.fixture
    def logged_client(self, client, user):
        client.login(username='testuser', password='pass12word')
        return client

    @pytest.fixture
    def label(self):
        return Label.objects.create(name='Label')

    def test_label_list_view(self, logged_client, label):
        response = logged_client.get(reverse('labels'))
        assert response.status_code == 200
        assert 'Label' in response.content.decode()

    def test_create_label(self, logged_client):
        response = logged_client.post(
            reverse('labels_create'),
            {'name': 'New label'}
            )
        assert response.status_code == 302
        assert Label.objects.filter(name='New label').exists()

    def test_update_label(self, logged_client, label):
        response = logged_client.post(
            reverse('labels_update', args=[label.id]),
            {'name': 'Newer label'}
            )
        assert response.status_code == 302
        label.refresh_from_db()
        assert label.name == 'Newer label'

    def test_delete_unused_label(self, logged_client, label):
        response = logged_client.post(reverse('labels_delete', args=[label.id]))
        assert response.status_code == 302
        assert not Label.objects.filter(id=label.id).exists()

    def test_delete_used_label_protected(self, logged_client, label, user):
        status = Status.objects.create(name='Статус')
        task = Task.objects.create(name='Main task', author=user, status=status)
        task.labels.add(label)

        response = logged_client.post(reverse('labels_delete', args=[label.id]))
        assert response.status_code == 302
        assert Label.objects.filter(id=label.id).exists()
