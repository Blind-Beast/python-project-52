from django.test import TestCase
from .models import Label

class LabelsTest(TestCase):

    def setUp(self):
        self.label = Label.objects.create(name="Test label")
    
    def test_label_created(self):
        label = Label.objects.filter(name="Test label")
        self.assertTrue(label.exists())
