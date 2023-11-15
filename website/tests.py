from unittest.mock import Mock, patch

from django.contrib import messages
from django.test import TestCase
from django.urls import reverse

from .forms import SignUpForm, SignUpFormGroup
from .views import login_user


class UserRegistrationFormTest(TestCase):

    def test_valid_registration_data(self):
        form = SignUpForm({
            'username': 'testuser',
            'first_name': 'deshan',
            'last_name': 'salitha',
            'registration_trype': '0',
            'email': 'testuser@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        })
        self.assertTrue(form.is_valid())

    def test_invalid_email(self):
        form = SignUpForm({
            'username': 'test_user',
            'first_name': 'deshan',
            'last_name': 'salitha',
            'registration_trype': '0',
            'email': 'testuserexample.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'])

    def test_mismatched_passwords(self):
        form = SignUpForm({
            'username': 'testuser',
            'first_name': 'deshan',
            'last_name': 'salitha',
            'registration_trype': '0',
            'email': 'testuser@example.com',
            'password1': 'testpassword1',
            'password2': 'testpassword2'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], ['The two password fields didn’t match.'])


class GroupRegistrationFormTest(TestCase):

    def test_valid_registration_data(self):
        form = SignUpFormGroup({
            'name': 'Test Group',
            'representative_user': 1,  # Assuming user with id 1 exists
        })
        self.assertTrue(form.is_valid())


class LoginUser(TestCase):
    def setUp(self):
        self.request = Mock()
        self.request.method = 'POST'
        self.request.POST.set('username', 'testuser')
        self.request.POSTset('password', 'testpassword')


    def test_login_successful(self, mock_authenticate):
        mock_authenticate.return_value = Mock(spec=['testsuser,testpassword'])
        response = login_user(self.request)
        self.assertEqual(messages.success.call_args[1][0], 'You have been logged in!')
        self.assertRedirects(response, reverse('home'))

