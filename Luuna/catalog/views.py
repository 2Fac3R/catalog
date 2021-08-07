from catalog.models import Product
from django.shortcuts import render
from django.views import generic
from .models import Product

def index(request):
    """View function for home page of site."""
    # Generate number of products
    num_products = Product.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    # Unread notifications
    if request.user.is_authenticated:
        notifications_unread = request.user.notifications.unread()
    else:
        notifications_unread = None

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html',
        context = {
            'num_products': num_products,
            'num_visits': num_visits,
            'notifications_unread': notifications_unread
        },
    )

class ProductListView(generic.ListView):
    """Generic class-based view for a list of products."""
    model = Product
    paginate_by = 10
    ordering = ['id']


class ProductDetailView(generic.DetailView):
    """Generic class-based detail view for a product."""
    model = Product
