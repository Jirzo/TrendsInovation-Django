from django.db import models

class Comment(models.Model):
    comment_author = models.CharField(max_length=30)
    comment_content = models.CharField(max_length=120)
    comment_status = models.BooleanField('Status', default=False)
    created_at = models.DateTimeField('Date creation',auto_now_add=True, null=False)
    updated_at = models.DateTimeField('Date updated', auto_now=True, null=False)

    def __str__(self):
        return f'{self.comment_author}'
