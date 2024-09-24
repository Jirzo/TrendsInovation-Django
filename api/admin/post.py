from django.contrib import admin
from api.models.post import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'post_title', 'post_description',
                    'created_at', 'updated_at')
