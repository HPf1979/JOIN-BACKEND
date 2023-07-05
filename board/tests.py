from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from board.models import Todo


class LoginUserTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            'andre@gmail.com', password='andre')
        self.client.login(username='andre@gmail.com', password='andre')

    def test_login_success(self):
        url = reverse('api-login')
        data = {
            'username': 'andre@gmail.com',
            'password': 'andre',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TodoListViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_todos(self):
        url = reverse('todos')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_todo(self):
        url = reverse('todos')
        data = {
            'title': 'Test Todo',
            'description': 'This is a test todo',
            'status': 'pending'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
