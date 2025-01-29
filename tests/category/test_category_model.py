from django.test import TestCase, Client
from api.models import Categories
import json

class TestCategoryModel(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Categories.objects.create(
            category_name='Category one',
            category_description='Category one description',
            category_status=True,
        )
        self.single_category_url = f'http://127.0.0.1:8000/api/v1/category/item/{
            self.category.id}'

    def test_model_category_POST(self):
        category_item = Categories.objects.create(
            category_name='Category one',
            category_description='Category one description',
            category_status=True,
        )
        self.assertEqual(str(category_item), 'Category one')
        self.assertTrue(isinstance(category_item, Categories))

    def test_model_category_PATCH(self):
        category_item_modification = {
            "category_name": "Horror test",
            "category_description": self.category.category_description,
            "category_status": self.category.category_status,
            "created_at": self.category.created_at,
            "updated_at": self.category.updated_at
        }
        response = self.client.patch(
            self.single_category_url,
            data=category_item_modification,
            content_type='application/json')
        contenResponse = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(contenResponse['message'], 'Category updated successfully')

        # Validar que el usuario fue actualizado
        self.category.refresh_from_db()
        self.assertEqual(self.category.category_name, 'Horror test')

    def test_model_category_DELETE(self):
        #Verificar que el usuario exista
        self.assertTrue(Categories.objects.filter(id=self.category.id).exists())

        response = self.client.delete(self.single_category_url)
        contentResponse = json.loads(response.content)

        self.assertEqual(response.status_code, 202)
        self.assertEqual(contentResponse['message'], 'Category deleted successfully')
        self.assertFalse(Categories.objects.filter(id=self.category.id).exists())
