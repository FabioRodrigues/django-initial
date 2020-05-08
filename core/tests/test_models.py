from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    def test_crete_user_with_email_successful(self):
        email='fabio.rodrigues018@gmail.com'
        password='password123'
        user=get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email,email)