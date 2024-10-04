from django.test import TestCase, Client
from api.models import Categories


class TestModels(TestCase):
    def test_model_category(self):
        category_item = Categories.objects.create(
            category_name='Category one',
            category_description='Category one description',
            category_status=True,
        )
        self.assertEquals(str(category_item), 'Category one')
        self.assertTrue(isinstance(category_item, Categories))
