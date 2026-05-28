from django.test import TestCase, Client
from django.urls import reverse
from api.models import Categories
import json

class TestCategoryViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.categories_url = reverse('api:category_api')
        self.category = Categories.objects.create(category_name='Category one',
                                                  category_description='Category one description',
                                                  category_status=True,)
        self.single_category_url = f'http://127.0.0.1:8000/api/v1/category/item/{
            self.category.id}'  

    def test_category_GET(self):
        # mock the response
        response = self.client.get(self.categories_url)
        contentMessage = json.loads(response.content)['status']
        # write the assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(contentMessage, 'success')

    def test_category_GET_single_item(self):
        # mock the response
        response = self.client.get(self.single_category_url)
        contentMessage = json.loads(response.content)
        # write the assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(contentMessage['status'], 'success')
        # Check the content
        self.assertEqual(contentMessage['data']['id'], self.category.id)
        self.assertEqual(
            contentMessage['data']['category_name'], self.category.category_name)
    # def test_category_GET_400_error(self):
    #     # mock the response
    #     response = self.client.get(self.categories_url)
    #     contentMessage = json.loads(response.content)['status']
    #     # write the assertions
    #     self.assertEqual(response.status_code, 400)
    #     self.assertEqual(contentMessage, 'success')