from django.test import TestCase
from apps.users.models import User


class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='aziz_master1',
            bio='i am daun',
            age=16,
            gender='man',
        )
