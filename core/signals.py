from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import QuoteRequest

@receiver(post_save, sender=QuoteRequest)
def send_quote_email(sender, instance, created, **kwargs):
    if created:
        # Logic to map IP to email (e.g., lookup table or external API)
        user_email = instance.company_email 
        subject = "Your BWell Quote Submission"
        message = f"Thank for submitting! We’ll contact you soon."
        send_mail(subject, message, "nasrukhan2070@gmail.com", [user_email])
