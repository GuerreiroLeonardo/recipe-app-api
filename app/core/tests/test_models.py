from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        ''' test creating a new user with an email is succsfull'''
        email = "leoenav@gmail.com"
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email = email,
            password=password
        )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password)) #check_password is a helper function that comer with the django_user_model
                                                       #Returns true if is correct and false if it is not correct.

    def test_new_user_email_normalized(self):
        '''test the email for a new user is normalized'''
        email = 'leoenav@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        '''test creating user with no email raises error'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        '''Test creating a new superuser'''
        user = get_user_model().objects.create_superuser(
            'leoenav@gmail.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
