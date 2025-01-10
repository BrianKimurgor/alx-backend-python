from django.contrib import admin
from .models import Message, MessageHistory

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("sender", "receiver", "timestamp", "edited", "edited_at", "edited_by")
    list_filter = ("edited", "timestamp")
    search_fields = ("content", "sender__username", "receiver__username")

@admin.register(MessageHistory)
class MessageHistoryAdmin(admin.ModelAdmin):
    list_display = ("original_message", "changed_at")
    search_fields = ("old_content",)
