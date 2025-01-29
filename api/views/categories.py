from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models import Categories
from ..serializers.categorySerializer import CategorySerializer


class CategoryAPIList(APIView):
    def get_user_by_id(self, id):
        """
        Helper function to fetch a user by ID or return 404 if not found.
        """
        return get_object_or_404(Categories, id=id)

    def get(self, request, id=None):
        if id:
            category = self.get_user_by_id(id)
            categories_serializer = CategorySerializer(category)
            return Response(
                {"status": "success", "data": categories_serializer.data}, 
                status=status.HTTP_200_OK
            )
        categories = Categories.objects.all()
        categories_serializer = CategorySerializer(categories, many=True)
        return Response(
            {"status": "success", "data": categories_serializer.data}, 
            status=status.HTTP_200_OK
        )

    def post(self, request):
        categories_serializer = CategorySerializer(data=request.data)
        if categories_serializer.is_valid():
            categories_serializer.save()
            return Response(
                {"status": "success", "message": "Category created successfully", "data": categories_serializer.data}, 
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"status": "error", "message": "Invalid data", "errors": categories_serializer.errors}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, id=None):
        category = self.get_user_by_id(id)
        categories_serializer = CategorySerializer(
            category, data=request.data, partial=True
        )
        if categories_serializer.is_valid():
            categories_serializer.save()
            return Response(
                {"status": "success", "message": "Category updated successfully", "data": categories_serializer.data}, 
                status=status.HTTP_200_OK
            )
        return Response(
            {"status": "error", "message": "Invalid data", "errors": categories_serializer.errors}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, id=None):
        category = get_object_or_404(Categories, id=id)
        category.delete()
        return Response(
            {"status": "success", "message": "Category deleted successfully"}, 
            status=status.HTTP_202_ACCEPTED
        )
