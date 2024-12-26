from django.contrib import admin
from .models import CustomUser, ChatRoom, ChatMessage

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(ChatRoom)
admin.site.register(ChatMessage)