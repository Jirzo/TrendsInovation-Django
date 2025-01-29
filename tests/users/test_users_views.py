from django.test import TestCase, Client
from django.urls import reverse
from api.models import User
import json


class TestUsersViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_url = reverse('api:comment_api')
        self.user_instance = User.objects.create(
            first_name='Fist test name',
            last_name='Last test name',
            email='test@gmail.com',
            psw='1234567890',
            user_status=True,
        )
        self.single_user_url = f'http://127.0.0.1:8000/api/v1/user/item/{
            self.user_instance.id}'  

    def test_user_GET(self):
        response = self.client.get(self.user_url)
        contentMessage = json.loads(response.content)['status']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(contentMessage, 'success')

    def test_user_GET_single_item(self):
        response = self.client.get(self.single_user_url)
        contentMessage = json.loads(response.content)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(contentMessage['status'], 'success')

        self.assertEqual(contentMessage['data']['id'], self.user_instance.id)
        self.assertEqual(contentMessage['data']['email'], self.user_instance.email)
