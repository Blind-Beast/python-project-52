from django.test import TestCase
from django.urls import reverse

class TasksTest(TestCase):
    def test_tasks_list(self):
        response = self.client.get(reverse("tasks"))
        self.assertEqual(response.status_code, 200)
