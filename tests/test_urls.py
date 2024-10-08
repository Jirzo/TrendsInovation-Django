from api.urls import urlpatterns
from django.test import TestCase, Client
import json


class TestUrls(TestCase):
    def setUp(self):
        self.client = Client()
        self.categories_url = 'http://127.0.0.1:8000/api/v1/category'

    def test_category_GET(self):
        # mock the response
        response = self.client.get(self.categories_url)
        # write the assertions
        self.assertEquals(response.status_code, 200)

