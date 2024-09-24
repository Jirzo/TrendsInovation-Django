from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Comment
from ..serializers.commentSerializer import CommentSerializer


class CommentAPIList(APIView):

    def get(self, request, id=None):
        if (id):
            comment = Comment.objects.get(id=id)
            comment_serializer = CommentSerializer(comment)
            return Response({"status": "success", "data": comment_serializer.data}, status=status.HTTP_200_OK)
        categories = Comment.objects.all()
        comment_serializer = CommentSerializer(categories, many=True)
        return Response({"status": "success", "data": comment_serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        comments_serializer = CommentSerializer(data=request.data)
        if comments_serializer.is_valid():
            comments_serializer.save()
            return Response({"status": "success", "data": comments_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": comments_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        category = Comment.objects.get(id=id)
        comments_serializer = CommentSerializer(
            category, data=request.data, partial=True)
        if comments_serializer.is_valid():
            comments_serializer.save()
            return Response({"status": "success", "data": comments_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": comments_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        category = Comment.objects.filter(id=id)
        print(category)
        category.delete()
        return Response({"status": "success", "data": "Item Deleted"})
