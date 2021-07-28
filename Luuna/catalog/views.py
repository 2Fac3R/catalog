from catalog.models import Product
from django.shortcuts import render
from django.views import generic
from .models import Product

def index(request):
    """View function for home page of site."""
    # Generate number of products
    num_products = Product.objects.all().count()

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context = {
            'num_products': num_products,
        },
    )

class ProductListView(generic.ListView):
    """Generic class-based view for a list of products."""
    model = Product
    paginate_by = 10


class ProductDetailView(generic.DetailView):
    """Generic class-based detail view for a product."""
    model = Product
