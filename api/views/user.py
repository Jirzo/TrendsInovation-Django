from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from ..models import User
from ..serializers.userSerializer import UserSerializer


class UserAPIList(APIView):

    def get(self, request, id=None):
        if (id):
            try:
                user = User.objects.get(id=id)
            except User.DoesNotExist:
                return Response({"status": "User not found"}, status=status.HTTP_404_NOT_FOUND)
            user_serializer = UserSerializer(user)
            return Response({"status": "success", "data": user_serializer.data}, status=status.HTTP_200_OK)
        categories = User.objects.all()
        user_serializer = UserSerializer(categories, many=True)
        return Response({"status": "success", "data": user_serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        users_serializer = self.UserSerializer(data=request.data)
        if users_serializer.is_valid():
            users_serializer.save()
            return Response({"status": "User Created", "data": users_serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"status": "error", "data": users_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        try:
            category = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({"status": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        users_serializer = UserSerializer(
            category, data=request.data, partial=True)
        if users_serializer.is_valid():
            users_serializer.save()
            return Response({"status": "User modified", "data": users_serializer.data}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"status": "error", "data": users_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        try:
            category = User.objects.filter(id=id)
        except User.DoesNotExist:
            return Response({"status": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
