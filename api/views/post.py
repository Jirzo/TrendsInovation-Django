from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Post
from ..serializers.postSerializer import PostSerializer


class PostAPIList(APIView):

    def get(self, request, id=None):
        if (id):
            post = Post.objects.get(id=id)
            post_serializer = PostSerializer(post)
            return Response({"status": "success", "data": post_serializer.data}, status=status.HTTP_200_OK)
        categories = Post.objects.all()
        post_serializer = PostSerializer(categories, many=True)
        return Response({"status": "success", "data": post_serializer.data}, status=status.HTTP_200_OK)


    def post(self, request):
        print(request.data)
        posts_serializer = PostSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response({"status": "success", "data": posts_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": posts_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        category = Post.objects.get(id=id)
        posts_serializer = PostSerializer(
            category, data=request.data, partial=True)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response({"status": "success", "data": posts_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": posts_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        category = Post.objects.filter(id=id)
        print(category)
        category.delete()
        return Response({"status": "success", "data": "Item Deleted"})