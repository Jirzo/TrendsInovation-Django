from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models import User
from ..serializers.userSerializer import UserSerializer, UserListSerializer


class UserAPIList(APIView):
    def get_user_by_id(self, id):
        """
        Helper function to fetch a user by ID or return 404 if not found.
        """
        return get_object_or_404(User, id=id)

    def get(self, request, id=None):
        if id:
            user = self.get_user_by_id(id)
            user_serializer = UserListSerializer(user)
            return Response(
                {"status": "success", "data": user_serializer.data}, 
                status=status.HTTP_200_OK
            )
        users = User.objects.all()
        user_serializer = UserListSerializer(users, many=True)
        return Response(
            {"status": "success", "data": user_serializer.data}, 
            status=status.HTTP_200_OK
        )

    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(
                {"status": "User Created", "data": user_serializer.data}, 
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"status": "error", "data": user_serializer.errors}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, id=None):
        user = self.get_user_by_id(id)
        user_serializer = UserSerializer(user, data=request.data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(
                {"status": "User modified", "data": user_serializer.data}, 
                status=status.HTTP_202_ACCEPTED
            )
        return Response(
            {"status": "error", "data": user_serializer.errors}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, id=None):
        user = self.get_user_by_id(id)
        user.delete()
        return Response(
            {"status": "User deleted"}, 
            status=status.HTTP_202_ACCEPTED
        )
