from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@email.com', password='pass123'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


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

    def test_tag_string(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)

    def test_tag_string(self):
        """Test the tag string representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_string(self):
        """Test the recipe stirng representation"""
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='Streak and mushroom sauce',
            time_minutes=5,
            price=5.00
        )
        self.assertEqual(str(recipe), recipe.title)