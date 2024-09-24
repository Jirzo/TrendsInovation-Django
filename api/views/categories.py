from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Categories
from ..serializers.categorySerializer import CategorySerializer


class CategoryAPIList(APIView):

    def get(self, request, id=None):
        if (id):
            category = Categories.objects.get(id=id)
            categories_serializer = CategorySerializer(category)
            return Response({"status": "success", "data": categories_serializer.data}, status=status.HTTP_200_OK)
        categories = Categories.objects.all()
        categories_serializer = CategorySerializer(categories, many=True)
        return Response({"status": "success", "data": categories_serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.data)
        categories_serializer = CategorySerializer(data=request.data)
        if categories_serializer.is_valid():
            categories_serializer.save()
            return Response({"status": "success", "data": categories_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": categories_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        category = Categories.objects.get(id=id)
        categories_serializer = CategorySerializer(
            category, data=request.data, partial=True)
        if categories_serializer.is_valid():
            categories_serializer.save()
            return Response({"status": "success", "data": categories_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": categories_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        category = Categories.objects.filter(id=id)
        print(category)
        category.delete()
        return Response({"status": "success", "data": "Item Deleted"})
