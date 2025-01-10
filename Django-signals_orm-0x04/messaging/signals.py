from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.timezone import now
from .models import Message, MessageHistory

@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.pk:  # Only check for updates (not new messages)
        try:
            old_message = Message.objects.get(pk=instance.pk)
            if old_message.content != instance.content:
                # Log the old content
                MessageHistory.objects.create(
                    original_message=old_message,
                    old_content=old_message.content,
                )
                # Update edited fields
                instance.edited = True
                instance.edited_at = now()
        except Message.DoesNotExist:
            pass  # Message is new, no history to log
