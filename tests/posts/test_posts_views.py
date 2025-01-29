from django.test import TestCase, Client
from django.urls import reverse
from api.models import Categories
import json

class TestPostsViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.post_url = reverse('api:comment_api')

    def test_post_url(self):
        response = self.client.get(self.post_url)
        contentMessage = json.loads(response.content)['status']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(contentMessage, 'success')