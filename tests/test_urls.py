from api.urls import urlpatterns 
from django.test import TestCase, Client

class BasicTest(TestCase):

    def test_category_status_code(self, client):
        response = client.get('/category')
        print(response)
        assert response.status_code == 200