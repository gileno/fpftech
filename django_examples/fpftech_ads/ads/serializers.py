from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['id', 'title', 'created']
        model = Category
