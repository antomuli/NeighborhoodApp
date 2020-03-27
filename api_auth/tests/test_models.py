from django.test import TestCase
from mimesis import Generic

from ..models import User


class UserModelTestCase(TestCase):
    def setUp(self):
        self.gen = Generic()
        self.new_user = User(
            first_name=self.gen.person.full_name().split()[0],
            last_name=self.gen.person.full_name().split()[1],
            email=self.gen.person.email(),
            raw_password=self.gen.person.password()
        )

    def test_user_instance(self):
        self.assertIsInstance(self.new_user, User)