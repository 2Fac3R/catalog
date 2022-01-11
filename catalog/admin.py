"""Admin Site."""

# Django
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Catalog
from .models import Product


# Unregister the provided model admin
admin.site.unregister(User)

# Register our own model admin, based on the default UserAdmin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'price', 'brand')
    list_filter = ('name', 'brand')
    search_fields = ('sku', 'name')
