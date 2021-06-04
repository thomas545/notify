from model_bakery import baker
from rest_framework.test import APITestCase


class UserModelTestCase(APITestCase):
    def test_user(self):
        user = baker.make("users.User")
        self.assertEqual(user.__str__(), user.username)
