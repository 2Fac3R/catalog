from catalog.models import Product
from django.shortcuts import render
from django.views import generic

from django.contrib.auth.models import User, Group

from rest_framework import viewsets, permissions

from .serializers import GroupSerializer, UserSerializer, ProductSerializer 
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


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('id')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer