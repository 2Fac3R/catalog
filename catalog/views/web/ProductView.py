"""Product View."""

# Django
from django.views import generic

# Catalog
from catalog.models import Product


class ProductListView(generic.ListView):
    """Generic class-based view for a list of products."""
    model = Product
    paginate_by = 10
    ordering = ['id']


class ProductDetailView(generic.DetailView):
    """Generic class-based detail view for a product."""
    model = Product
