from django.test import TestCase
from rest_framework import status
from mimesis import Generic

from ..models import User


class SignUpViewTestCase(TestCase):
    def setUp(self):
        self.gen = Generic()
        self.payload = {
            'first_name': self.gen.person.full_name().split()[0],
            'last_name': self.gen.person.full_name().split()[1],
            'email': self.gen.person.email(),
            'password': self.gen.person.password()
        }

    def test_signup_view_with_data(self):
        response = self.client.post(
            '/auth/signup',
            data=self.payload
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_sign_view_without_data(self):
        response = self.client.post(
            '/auth/signup',
            data={}
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_already_exists_signup(self):
        self.client.post('/auth/signup', data=self.payload)
        response = self.client.post('/auth/signup', data=self.payload)

        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

    def tearDown(self):
        User.objects.all().delete()


class LoginViewTestCase(TestCase):
    def setUp(self):
        self.gen = Generic()
        self.payload = {
            'first_name': self.gen.person.full_name().split()[0],
            'last_name': self.gen.person.full_name().split()[1],
            'email': self.gen.person.email(),
            'password': self.gen.person.password()
        }
        self.client.post('/auth/signup', data=self.payload)
    
    def test_login_successfull(self):
        response = self.client.post(
            '/auth/login',
            data={
                'email': self.payload['email'],
                'password': self.payload['password']
            },
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.json())
        self.assertIn('refresh', response.json())

    def test_login_failed(self):
        response = self.client.post(
            '/auth/login',
            data={
                'email': self.payload['email'],
                'password': self.payload['password']+'123'
            },
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_login_data_none(self):
        response = self.client.post('/auth/login')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def tearDown(self):
        User.objects.all().delete()


class RefreshTokenViewTestCase(TestCase):
    def setUp(self):
        self.gen = Generic()
        self.payload = {
            'first_name': self.gen.person.full_name().split()[0],
            'last_name': self.gen.person.full_name().split()[1],
            'email': self.gen.person.email(),
            'password': self.gen.person.password()
        }
        self.client.post('/auth/signup', data=self.payload)
        self.login_response = self.client.post('/auth/login',
            data={
                'email': self.payload['email'],
                'password': self.payload['password']
            }
        )

    def test_refresh_token(self):
        response = self.client.post(
            '/auth/token/refresh',
            data={
                'access': self.login_response.json()['refresh']
            }
        )

        self.assertIn('refresh', response.json())

    def tearDown(self):
        User.objects.all().delete()