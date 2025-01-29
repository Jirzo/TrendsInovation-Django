from django.test import TestCase, Client
from api.models import Comment

class TestCommentsModel(TestCase):
    print("Comment")
    def test_model_comment(self):
        comment_item = Comment.objects.create(
            comment_author='Comment one',
            comment_content='Comment content',
            comment_status=False,
        )
        self.assertEqual(str(comment_item), 'Comment one')
        self.assertTrue(isinstance(comment_item, Comment))

