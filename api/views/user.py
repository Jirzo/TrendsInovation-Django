from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import User
from ..serializers.userSerializer import UserSerializer


class UserAPIList(APIView):

    def get(self, request, id=None):
        if (id):
            user = User.objects.get(id=id)
            user_serializer = UserSerializer(user)
            return Response({"status": "success", "data": user_serializer.data}, status=status.HTTP_200_OK)
        categories = User.objects.all()
        user_serializer = UserSerializer(categories, many=True)
        return Response({"status": "success", "data": user_serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.data)
        users_serializer = UserSerializer(data=request.data)
        if users_serializer.is_valid():
            users_serializer.save()
            return Response({"status": "success", "data": users_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": users_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        category = User.objects.get(id=id)
        users_serializer = UserSerializer(
            category, data=request.data, partial=True)
        if users_serializer.is_valid():
            users_serializer.save()
            return Response({"status": "success", "data": users_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": users_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        category = User.objects.filter(id=id)
        print(category)
        category.delete()
        return Response({"status": "success", "data": "Item Deleted"})