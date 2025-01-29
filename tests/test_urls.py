from api.urls import urlpatterns
from django.test import TestCase, Client
import json


class TestUrls(TestCase):
    def setUp(self):
        self.client = Client()
        self.categories_url = 'http://127.0.0.1:8000/api/v1/category'
        self.comment_url = 'http://127.0.0.1:8000/api/v1/comment'
        self.user_url = 'http://127.0.0.1:8000/api/v1/user'
        self.post_url = 'http://127.0.0.1:8000/api/v1/post'

    def test_category_GET(self):
        # mock the response
        response = self.client.get(self.categories_url)
        # write the assertions
        self.assertEqual(response.status_code, 200)

    def test_comment_GET(self):
        response = self.client.get(self.comment_url)
        self.assertEqual(response.status_code, 200)

    def test_post_GET(self):
        response = self.client.get(self.post_url)
        self.assertEqual(response.status_code, 200)
    
    def test_user_GET(self):
        response = self.client.get(self.user_url)
        self.assertEqual(response.status_code, 200)
