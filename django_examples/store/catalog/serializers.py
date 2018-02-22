from rest_framework import serializers

from .models import Product, Category


class ProductModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'quantity', 'created', 'modified'
        ]


class ProductSerializer(serializers.Serializer):

    name = serializers.CharField()
    description = serializers.CharField()
    quantity = serializers.IntegerField()

    def validate_name(self, value):
        if 'DRF' in value:
            raise serializers.ValidationError('Não pode conter DRF')
        return value


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'created', 'modified']
