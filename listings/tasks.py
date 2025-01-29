from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_booking_confirmation_email(user_email, booking_details):
    """
    Sends a booking confirmation email asynchronously.
    """
    subject = "Booking Confirmation"
    message = f"Dear Customer,\n\nYour booking has been confirmed.\n\nDetails:\n{booking_details}\n\nThank you!"
    sender_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]

    send_mail(subject, message, sender_email, recipient_list)
    return f"Email sent to {user_email}"
