from rest_framework import serializers

from .models import Category, Ad


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['id', 'title', 'created']
        model = Category


class AdSerializer(serializers.ModelSerializer):

    class Meta:
        fields = [
            'id', 'title', 'user', 'category', 'description',
            'offer_type', 'created', 'modified',
        ]
        read_only_fields = ['user']
        model = Ad
