from django.test import TestCase, Client
from motus.models import User


class MyData(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

        cls.admin_user = User.objects.create_superuser(
            username="admin", password="admin", is_staff=True, is_superuser=True
        )
        cls.user = User.objects.create_user(
            username="user",
            password="motuslife13*",
            is_staff=True,
        )
        cls.user_two = User.objects.create_user(
            username="user_two",
            password="motuslife13*",
            is_staff=True,
        )
