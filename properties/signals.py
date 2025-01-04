from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Inquiries
from decouple import config

@receiver(post_save, sender=Inquiries, dispatch_uid="send_email_to_agent")
def send_email_to_agent(sender, instance, created, *args, **kwargs):
    if created:
        agent = instance.property.agent
        subject = f"New Inquiry for {instance.property.name}"
        message = f"""
        Dear {agent.name},

        You have received a new inquiry for the property '{instance.property.name}'.

        Inquiry Details:
        Name: {instance.name}
        Email: {instance.email}
        Phone: {instance.phone}
        Message: {instance.message}

        Please log in to the system to view more details.

        Thank you,
        PrimeYard Team
        """
        recipient_list = [agent.email]
        send_mail(subject, message, config("EMAIL_HOST_USER"), recipient_list)
