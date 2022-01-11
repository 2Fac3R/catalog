"""Catalog app config."""

# Django
from django.apps import AppConfig


class CatalogConfig(AppConfig):
    name = 'catalog'

    def ready(self):
        pass
        # import catalog.signals.notify_admins
