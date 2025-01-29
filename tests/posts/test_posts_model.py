from django.test import TestCase, Client
from api.models import Categories, Comment, User, Post
import json


class TestPostsModel(TestCase):
    def setUp(self):
        self.client = Client()

        self.category = Categories.objects.create(
            category_name="Test Category")
        self.comment = Comment.objects.create(comment_author="Test Comment")
        self.user = User.objects.create(
            first_name="Test User", email="testuser@example.com")
        self.post_item = Post.objects.create(
            post_title='First test Post',
            post_description="First test post description",
            image='',
            category_fk=self.category,
            comments_fk=self.comment,
            user_fk=self.user,
        )
        self.single_post_url = f'http://127.0.0.1:8000/api/v1/post/item/{
            self.post_item.id}'

    def test_model_post_POST(self):
        # Asegurarte de que el objeto se creó correctamente
        self.assertEqual(str(self.post_item), 'First test Post')
        self.assertTrue(isinstance(self.post_item, Post))

    def test_model_post_PATCH(self):
        post_item_modification = {
            'post_title': 'First test',
            'post_description': "First test post",
            'image': self.post_item.image,
            'category_fk': self.post_item.category_fk,
            'comments_fk': self.post_item.comments_fk,
            'user_fk': self.post_item.user_fk,
            "created_at": self.post_item.created_at,
            "updated_at": self.post_item.updated_at,
        }
        response = self.client.patch(
            self.single_post_url,
            data=post_item_modification,
            content_type='application/json'
        )
        contenResponse = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(contenResponse['status'], 'success')

        self.post_item.refresh_from_db()
        self.assertEqual(self.post_item.post_title, 'First test')
        self.assertEqual(self.post_item.post_description, 'First test post')
