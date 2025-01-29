from django.test import TestCase, Client
from api.models import User
import json


class TestUsersModels(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(first_name='Fist test name',
                                        last_name='Last test name',
                                        email='test@gmail.com',
                                        psw='1234567890',
                                        user_status=True,)
        self.single_user_url = f'http://127.0.0.1:8000/api/v1/user/item/{
            self.user.id}'

    def test_model_user_POST(self):
        user_item = User.objects.create(
            first_name='Fist test name',
            last_name='Last test name',
            email='test@gmail.com',
            psw='1234567890',
            user_status=True,
        )
        self.assertEqual(str(user_item), 'Fist test name')
        self.assertTrue(isinstance(user_item, User))

    def test_model_user_PATCH(self):
        user_item_modification = {
            'first_name': 'Fist test name modified',
            'last_name': 'Last test name modified',
            'email': self.user.email,
            'psw': self.user.psw,
            'user_status': self.user.user_status,
            "created_at": self.user.created_at,
            "updated_at": self.user.updated_at
        }
        response = self.client.patch(
            self.single_user_url,
            data = user_item_modification,
            content_type='application/json'
            )
        contentResponse = json.loads(response.content)

        self.assertEqual(response.status_code, 202)
        self.assertEqual(contentResponse['status'], 'User modified')

        # Validar que el usuario fue actualizado
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Fist test name modified')
        self.assertEqual(self.user.last_name, 'Last test name modified')

    def test_model_user_DELETE(self):
        # Verificar si el usuario existe
        self.assertTrue(User.objects.filter(id=self.user.id).exists())

        response = self.client.delete(self.single_user_url)
        print(f'hhhhhhhhhhh {response}')
        contenResponse = json.loads(response.content)

        self.assertEqual(response.status_code, 202)
        self.assertEqual(contenResponse['status'], 'User deleted')
        
        # Verificar si el usuario se elimino
        self.assertFalse(User.objects.filter(id=self.user.id).exists())