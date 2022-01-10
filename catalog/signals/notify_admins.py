"""Signals: notify_admins"""

# Django
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Notifications
from notifications.signals import notify

# Catalog
from ..models import Product

# Utils
from ..utils import current_user


@receiver(post_save, sender=Product)
def notify_admins(sender, instance, **kwargs):
    """ Signal to notify admin users about post save in Product """
    admins_group = User.objects.filter(groups__name='admin')
    notify.send(
        current_user(),
        recipient=admins_group,
        verb='post_save',
        target=instance,
        description=f'{sender.__name__} ({instance.name}) was saved by {current_user()}.',
    )
