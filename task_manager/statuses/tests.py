from django.test import TestCase
from django.urls import reverse

class StatusesTest(TestCase):
    def test_statuses_list(self):
        response = self.client.get(reverse("statuses"))
        self.assertEqual(response.status_code, 200)
