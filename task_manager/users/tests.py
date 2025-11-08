from django.test import TestCase
from .models import CustomUser

class UserTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(username="John")
    
    def test_user_created(self):
        user = CustomUser.objects.filter(username="John")
        self.assertTrue(user.exists())