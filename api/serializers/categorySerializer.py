from rest_framework import serializers
from ..models.category import Categories


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

    def validate_empty_values(self, data):
        return super().validate_empty_values(data)

    def create(self, validated_data):
        return Categories.objects.create(**validated_data)