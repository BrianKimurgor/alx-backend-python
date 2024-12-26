from rest_framework import serializers
from .models import CustomUser, Conversation, Message


class CustomUserSerializer(serializers.ModelSerializer):
    """Serializer for the CustomUser model"""
    class Meta:
        model = CustomUser
        fields = ['user_id', 'username', 'email', 'first_name', 'last_name', 
                 'phone_number']
        read_only_fields = ['user_id']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        """Override create method to properly handle password hashing"""
        user = CustomUser.objects.create_user(**validated_data)
        return user


class MessageSerializer(serializers.ModelSerializer):
    """Serializer for the Message model"""
    sender_username = serializers.CharField(source='sender.username', read_only=True)

    class Meta:
        model = Message
        fields = ['message_id', 'conversation', 'sender', 'sender_username',
                 'message_body', 'sent_at']
        read_only_fields = ['message_id', 'sent_at', 'sender_username']


class ConversationSerializer(serializers.ModelSerializer):
    """Serializer for the Conversation model"""
    participants_detail = CustomUserSerializer(source='participants', 
                                            many=True, 
                                            read_only=True)
    last_message = serializers.SerializerMethodField()
    
    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'participants_detail',
                 'created_at', 'updated_at', 'last_message']
        read_only_fields = ['conversation_id', 'created_at', 'updated_at']

    def get_last_message(self, obj):
        """Get the last message in the conversation"""
        last_message = Message.objects.filter(conversation=obj).order_by('-sent_at').first()
        if last_message:
            return MessageSerializer(last_message).data
        return None


class ConversationDetailSerializer(ConversationSerializer):
    """Detailed serializer for single conversation view with messages"""
    messages = MessageSerializer(many=True, read_only=True, source='message_set')

    class Meta(ConversationSerializer.Meta):
        fields = ConversationSerializer.Meta.fields + ['messages']