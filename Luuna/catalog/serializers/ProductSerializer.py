""" Product Serializer."""

# Django
from catalog.models import Product

# Django Rest Framework
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['url', 'sku', 'name', 'price', 'brand']
