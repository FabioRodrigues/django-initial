from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email='fabio.rodrigues018@gmail.com'
        password='password123'
        user=get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_should_create_user_setting_email_lowercase(self):
        email = 'fabio@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'some_pass')

        self.assertEqual(user.email, email.lower())

    def test_should_raise_error_when_receiving_an_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test')

    def test_should_create_super_user(self):
        user = get_user_model().objects.create_superuser('fabio@gmail.com', 'password')
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
