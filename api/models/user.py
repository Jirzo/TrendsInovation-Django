from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=120)
    psw = models.CharField(max_length=30)
    user_status = models.BooleanField('Status', default=False)
    created_at = models.DateTimeField('Date creation',auto_now_add=True, null=False)
    updated_at = models.DateTimeField('Date updated', auto_now=True, null=False)

    def __str__(self):
        return f'{self.first_name}'