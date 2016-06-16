from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import Balance


@receiver(post_save, sender=User)
def create_settings(sender, instance, created, *args, **kwargs):
    if created:
        Balance.objects.create(owner=instance)
