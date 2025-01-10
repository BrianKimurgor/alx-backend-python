from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Message, MessageHistory


@receiver(pre_save, sender=Message)
def save_message_history(sender, instance, **kwargs):
    if instance.pk:  # Ensure this is an update, not a new message
        try:
            original_message = Message.objects.get(pk=instance.pk)
            if original_message.content != instance.content:
                # Save the old content in the MessageHistory model
                MessageHistory.objects.create(
                    message=original_message,
                    old_content=original_message.content
                )
                instance.edited = True  # Mark the message as edited
        except Message.DoesNotExist:
            pass  # This is a new message, no history needed
