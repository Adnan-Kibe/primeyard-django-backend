from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import User

@receiver(post_save, sender=User)
def send_otp(sender, instance, created, *args, **kwargs):
    pass