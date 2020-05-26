from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_succcessful(self):
        """Test if creating a new user with an email is successful"""
        email = 'test@email.com'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_with_normalized_email(self):
        """Test if user was created with a normalized email"""
        email = 'test@EMAIL.CoM'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())
        self.assertTrue(user.check_password(password))

    def test_create_user_with_invalid_email(self):
        """Test if creating an user with an invalid email raises an error"""

        with self.assertRaises(ValueError, message='This is an invalid email'):
            get_user_model().objects.create_user(
                email=None,
                password='Test123'
            )

    def test_create_superuser(self):
        """Test if a user has is_superuser and is_staff properties"""
        email = 'test@email.com'
        password = 'test123'
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
