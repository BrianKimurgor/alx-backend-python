from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Custom User Model
class CustomUser(AbstractUser):
    name = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    # profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.username


# Conversation Model
class Conversation(models.Model):
    participants = models.ManyToManyField(CustomUser, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.id}"


# Message Model
class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username}: {self.content[:20]}"
