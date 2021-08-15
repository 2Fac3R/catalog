from django.dispatch import receiver
from django.db.models.signals import post_save
from notifications.signals import notify

from django.contrib.auth.models import User
from .models import Product

from .utils import current_user

@receiver(post_save, sender=Product)
def notify_admins(sender, instance, **kwargs):
    """ Signal to notify admin users about post save in Product """
    admins_group = User.objects.filter(groups__name='admin')
    notify.send(
        current_user(),
        recipient=admins_group,
        verb='post_save',
        target=instance,
        description='{0} ({1}) was saved by {2}.'.format(sender.__name__, instance.name, current_user()),
    )
