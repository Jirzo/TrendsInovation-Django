from rest_framework import serializers
from ..models.user import User


class UserSerializer(serializers.ModelSerializer):
    psw = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def validate_email(self, value):
        if '@' not in value:
            raise serializers.ValidationError('Please enter a valid email.')
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                'Password must be at least 8 characters long.')
        return value
