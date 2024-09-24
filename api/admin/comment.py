from django.contrib import admin
from api.models.comment import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment_author', 'comment_content',
                    'comment_status', 'created_at', 'updated_at')
