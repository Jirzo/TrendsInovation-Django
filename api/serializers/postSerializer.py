from rest_framework import serializers
from ..models.post import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def validate_empty_values(self, data):
        return super().validate_empty_values(data)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
 