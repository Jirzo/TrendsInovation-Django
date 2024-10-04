from django.test import TestCase, Client
from django.urls import reverse
import json

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.categories_url = reverse('api:category_api')

    def test_category_GET(self):
        # mock the response
        response = self.client.get(self.categories_url)
        contentMessage = json.loads(response.content)['status']
        # write the assertions
        self.assertEquals(response.status_code, 200)
        self.assertEquals(contentMessage, 'success')
