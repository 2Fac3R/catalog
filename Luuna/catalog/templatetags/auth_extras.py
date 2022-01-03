"""Auth Extras."""

# Django
from django import template
from django.contrib.auth.models import Group


register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    """Check if the user is in a group."""
    group = Group.objects.get(name=group_name)
    return group in user.groups.all()
