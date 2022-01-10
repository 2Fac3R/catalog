""" Main urls conf."""

# Django
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.views.generic import RedirectView

# Django Rest Framework
from rest_framework import routers
from rest_framework import permissions

# drf-yasg - Yet another Swagger generator
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

# Catalog
from catalog.views.api import UserApiView as user_views
from catalog.views.api import GroupApiView as group_views
from catalog.views.api import ProductApiView as product_views

# Notifications
import notifications.urls

# Routing
router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewSet, basename='user')
router.register(r'groups', group_views.GroupViewSet, basename='group')
router.register(r'products', product_views.ProductViewSet, basename='product')

# API Conf
schema_view = get_schema_view(
    openapi.Info(
        title="Luuna API",
        default_version='v1',
        description="API Documentation",
        terms_of_service="127.0.0.1/#",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# Routes
urlpatterns = [
    # Catalog
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
    path('catalog/', include('catalog.urls')),
    # Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    # API
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    # Notifications
    path('inbox/notifications/',
         include(notifications.urls, namespace='notifications')),
    # API Documentation
    re_path(
        'swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
