""" Home view."""

# Django
from django.shortcuts import render

# Catalog
from catalog.models import Product


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
        context={
            'num_products': num_products,
            'num_visits': num_visits,
            'notifications_unread': notifications_unread
        },
    )
