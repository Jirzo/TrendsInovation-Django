from django.urls import path
from . import views


app_name = "api"
urlpatterns = [
    path('category', views.CategoryAPIList.as_view(), name='category_api'),
    path('category/item/<int:id>',
         views.CategoryAPIList.as_view(), name='single_category'),
    path('comment', views.CommentAPIList.as_view(), name='comment_api'),
    path('comment/item/<int:id>',
         views.CommentAPIList.as_view(), name='single_comment'),
    path('user', views.UserAPIList.as_view(), name='user_api'),
    path('user/item/<int:id>',
         views.UserAPIList.as_view(), name='single_user'),
    path('post', views.PostAPIList.as_view(), name='post_api'),
    path('post/item/<int:id>',
         views.PostAPIList.as_view(), name='single_post'),
]
