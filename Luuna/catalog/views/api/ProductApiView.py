"""Product API View"""

# Django Rest Framework
from rest_framework import viewsets

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Catalog
from catalog.models import Product
from catalog.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer

    # Filters
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('=sku', 'name', 'brand')
    filter_fields = ('sku', 'name', 'brand')
    ordering_fields = ['price']  # '__all__'
    ordering = ['-price']
