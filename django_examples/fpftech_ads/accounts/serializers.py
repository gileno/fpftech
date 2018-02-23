from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'name', 'date_joined',
            'is_staff', 'is_superuser'
        ]
        read_only_fields = ['username', 'is_staff', 'is_superuser']
