from django.contrib import admin
from api.models.category import Categories


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'category_description',
                    'category_status', 'created_at', 'updated_at')
