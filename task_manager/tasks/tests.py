from django.test import TestCase

from task_manager.users.models import CustomUser

from .models import Task


class TasksTest(TestCase):

    def setUp(self):
        self.user1 = CustomUser.objects.create(username="Author")
        self.user2 = CustomUser.objects.create(username="Executor")
        self.task = Task.objects.create(
            name="Test task",
            author=self.user1,
            executor=self.user2
        )
    
    def test_task_created(self):
        task = Task.objects.filter(name="Test task")
        self.assertTrue(task.exists())


