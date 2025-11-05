from django.test import TestCase
from django.urls import reverse

class UsersTest(TestCase):
    def test_users_list(self):
        response = self.client.get(reverse("users"))
        self.assertEqual(response.status_code, 200)