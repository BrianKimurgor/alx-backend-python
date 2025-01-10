from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Message, MessageHistory, Notification

@receiver(post_delete, sender=User)
def clean_up_user_data(sender, instance, **kwargs):
    """
    Deletes all related data when a user account is deleted.
    """
    # Delete all messages sent or received by the user
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()

    # Delete all message histories associated with the user's messages
    MessageHistory.objects.filter(original_message__sender=instance).delete()

    # Delete all notifications associated with the user
    Notification.objects.filter(user=instance).delete()
