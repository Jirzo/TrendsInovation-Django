from django.test import TestCase, Client
from django.urls import reverse
from api.models import Categories
import json

class TestCommentsViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.comment_url = reverse('api:comment_api')

    def test_comment_url(self):
        response = self.client.get(self.comment_url)
        contentMessage = json.loads(response.content)['status']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(contentMessage, 'success')