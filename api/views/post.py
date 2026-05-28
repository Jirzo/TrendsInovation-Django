from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models import Post, Categories, Comment, User
from ..serializers.postSerializer import PostSerializer


class PostAPIList(APIView):
    def get_post_by_id(self, id):
        """
        Helper function to fetch a Post by ID or return 404 if not found.
        """
        return get_object_or_404(Post.objects.select_related('category_fk', 'comments_fk', 'user_fk'), id=id)

    def get(self, request, id=None):
        if id:
            post = self.get_post_by_id(id)
            post_serializer = PostSerializer(post)
            return Response(
                {"status": "success", "data": post_serializer.data}, 
                status=status.HTTP_200_OK
            )
        # Optimized query for all posts with related data
        posts = Post.objects.select_related('category_fk', 'comments_fk', 'user_fk').all()
        post_serializer = PostSerializer(posts, many=True)
        return Response(
            {"status": "success", "data": post_serializer.data}, 
            status=status.HTTP_200_OK
        )

    def post(self, request):
        # Validate foreign key relations before saving
        category_id = request.data.get('category_fk')
        comment_id = request.data.get('comments_fk')
        user_id = request.data.get('user_fk')

        # Check if related models exist
        if not Categories.objects.filter(id=category_id).exists():
            return Response(
                {"status": "error", "message": f"Category with id {category_id} does not exist"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        if not Comment.objects.filter(id=comment_id).exists():
            return Response(
                {"status": "error", "message": f"Comment with id {comment_id} does not exist"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        if not User.objects.filter(id=user_id).exists():
            return Response(
                {"status": "error", "message": f"User with id {user_id} does not exist"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        post_serializer = PostSerializer(data=request.data)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(
                {"status": "success", "data": post_serializer.data}, 
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"status": "error", "data": post_serializer.errors}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, id=None):
        post = self.get_post_by_id(id)

        # Validate foreign key relations if provided
        category_id = request.data.get('category_fk_id')
        comment_id = request.data.get('comments_fk_id')
        user_id = request.data.get('user_fk_id')

        if category_id and not Categories.objects.filter(id=category_id).exists():
            return Response(
                {"status": "error", "message": f"Category with id {category_id} does not exist"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        if comment_id and not Comment.objects.filter(id=comment_id).exists():
            return Response(
                {"status": "error", "message": f"Comment with id {comment_id} does not exist"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        if user_id and not User.objects.filter(id=user_id).exists():
            return Response(
                {"status": "error", "message": f"User with id {user_id} does not exist"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        post_serializer = PostSerializer(post, data=request.data, partial=True)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(
                {"status": "success", "data": post_serializer.data}, 
                status=status.HTTP_200_OK
            )
        return Response(
            {"status": "error", "data": post_serializer.errors}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, id=None):
        post = self.get_post_by_id(id)
        post.delete()
        return Response(
            {"status": "success", "message": "Post deleted successfully"}, 
            status=status.HTTP_204_NO_CONTENT
        )
