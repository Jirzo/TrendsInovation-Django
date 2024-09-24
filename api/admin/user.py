from django.contrib import admin
from api.models.user import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',
                    'email', 'user_status', 'created_at', 'updated_at')
