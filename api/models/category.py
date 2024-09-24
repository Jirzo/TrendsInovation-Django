from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Categories(models.Model):
    category_name = models.CharField('Name Category',max_length=30, null=False)
    category_description = models.CharField('Description Categories', max_length=120, null=False)
    category_status = models.BooleanField('Status', default=False)
    created_at = models.DateTimeField('Date creation',auto_now_add=True, null=False)
    updated_at = models.DateTimeField('Date updated', auto_now=True, null=False)

    def __str__(self):
        return f'{self.category_name}'
