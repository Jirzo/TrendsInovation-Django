from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models import Comment, Post, User
from ..serializers.commentSerializer import CommentSerializer


class CommentAPIList(APIView):

    def get(self, request, id=None):
        if id:
            # Obtener comentario por ID con manejo de error 404
            comment = get_object_or_404(Comment, id=id)
            comment_serializer = CommentSerializer(comment)
            return Response(
                {"status": "success", "data": comment_serializer.data},
                status=status.HTTP_200_OK
            )
        # Obtener todos los comentarios
        comments = Comment.objects.all()
        comment_serializer = CommentSerializer(comments, many=True)
        return Response(
            {"status": "success", "data": comment_serializer.data},
            status=status.HTTP_200_OK
        )

    def post(self, request):
        """
        # Validar que el usuario asociado exista
        user_id = request.data.get('user_id')
        if not User.objects.filter(id=user_id).exists():
            return Response(
                {"status": "error", "message": "Invalid user ID"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Validar que el post asociado exista
        post_id = request.data.get('post_id')
        if not Post.objects.filter(id=post_id).exists():
            return Response(
                {"status": "error", "message": "Invalid post ID"},
                status=status.HTTP_400_BAD_REQUEST
            )
        """
        # Crear un nuevo comentario
        comment_serializer = CommentSerializer(data=request.data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response(
                {"status": "success", "data": comment_serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"status": "error", "data": comment_serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, id=None):
        # Obtener comentario
        comment = get_object_or_404(Comment, id=id)

        """
        # Validar que el usuario tenga permiso para editar el comentario
        user_id = request.data.get('user_id')
        if comment.user_id != user_id:
            return Response(
                {"status": "error",
                    "message": "You do not have permission to edit this comment"},
                status=status.HTTP_403_FORBIDDEN
            )
        """
        # Actualizar comentario
        comment_serializer = CommentSerializer(
            comment, data=request.data, partial=True)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response(
                {"status": "success", "data": comment_serializer.data},
                status=status.HTTP_200_OK
            )
        return Response(
            {"status": "error", "data": comment_serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, id=None):
        # Obtener comentario
        comment = get_object_or_404(Comment, id=id)

        # Validar que el usuario tenga permiso para eliminar el comentario
        """ user_id = request.data.get('user_id')
        if comment.user_id != user_id:
            return Response(
                {"status": "error", "message": "You do not have permission to delete this comment"},
                status=status.HTTP_403_FORBIDDEN
            )
        """
        # Eliminar comentario
        comment.delete()
        return Response(
            {"status": "success", "message": "Comment deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
