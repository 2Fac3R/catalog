from catalog.models import Product
from django.contrib import admin

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import Product


# Unregister the provided model admin
admin.site.unregister(User)

# Register our own model admin, based on the default UserAdmin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass

# Register model Product
admin.site.register(Product)