"""Catalog urls."""

# Django
from django.urls import path

# Catalog
from .views.web import HomeView as home_views
from .views.web import ProductView as product_views

urlpatterns = [
    path('', home_views.index, name='index'),
    path('products/', product_views.ProductListView.as_view(), name='products'),
    path('products/<int:pk>', product_views.ProductDetailView.as_view(),
         name='product-detail'),
]
