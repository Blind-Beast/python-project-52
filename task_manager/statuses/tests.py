from django.test import TestCase
from .models import Status

class StatusesTest(TestCase):

    def setUp(self):
        self.status = Status.objects.create(name="Test status")
    
    def test_status_created(self):
        status = Status.objects.filter(name="Test status")
        self.assertTrue(status.exists())

