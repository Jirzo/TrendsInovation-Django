from django.db import models
from .category import Categories
from .comment import Comment
from .user import User


class Post(models.Model):
    post_title = models.CharField(max_length=30)
    post_description = models.CharField(max_length=120)
    image = models.TextField(blank=True, null=True)
    category_fk = models.ForeignKey(Categories, models.DO_NOTHING)
    comments_fk = models.ForeignKey(Comment, models.DO_NOTHING)
    user_fk = models.ForeignKey(User, models.DO_NOTHING)
    created_at = models.DateTimeField('Date creation',auto_now_add=True, null=False)
    updated_at = models.DateTimeField('Date updated', auto_now=True, null=False)
    
    def __str__(self):
        return f'{self.post_title}'
