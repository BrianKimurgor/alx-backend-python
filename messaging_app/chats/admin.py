from django.contrib import admin
from .models import CustomUser, Conversation, ChatMessage

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Conversation)
admin.site.register(ChatMessage)