from django.test import TestCase
from django.urls import reverse

class LabelsTest(TestCase):
    def test_labels_list(self):
        response = self.client.get(reverse("labels"))
        self.assertEqual(response.status_code, 200)
