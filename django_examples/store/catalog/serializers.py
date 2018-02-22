from rest_framework import serializers

from .models import Product


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
