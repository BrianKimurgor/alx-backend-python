from django.test import TestCase
from django.contrib.auth.models import User
from messaging.models import Message, Notification


class MessagingAppTests(TestCase):
    def setUp(self):
        # Create test users
        self.sender = User.objects.create_user(username="sender", password="password123")
        self.receiver = User.objects.create_user(username="receiver", password="password123")
    
    def test_message_creation(self):
        """Test that a message can be created successfully."""
        message = Message.objects.create(
            sender=self.sender,
            receiver=self.receiver,
            content="Hello, this is a test message."
        )
        self.assertEqual(message.sender, self.sender)
        self.assertEqual(message.receiver, self.receiver)
        self.assertEqual(message.content, "Hello, this is a test message.")
        self.assertIsNotNone(message.timestamp)

    def test_notification_created_on_message(self):
        """Test that a notification is created when a message is sent."""
        # Send a message
        message = Message.objects.create(
            sender=self.sender,
            receiver=self.receiver,
            content="This message should trigger a notification."
        )

        # Check that a notification has been created for the receiver
        notification = Notification.objects.filter(user=self.receiver, message=message).first()
        self.assertIsNotNone(notification)
        self.assertEqual(notification.user, self.receiver)
        self.assertEqual(notification.message, message)
        self.assertFalse(notification.read)  # Ensure the notification is marked as unread

    def test_mark_notification_as_read(self):
        """Test that a notification can be marked as read."""
        # Send a message
        message = Message.objects.create(
            sender=self.sender,
            receiver=self.receiver,
            content="Mark this notification as read."
        )

        # Get the notification
        notification = Notification.objects.get(user=self.receiver, message=message)
        self.assertFalse(notification.read)

        # Mark as read
        notification.read = True
        notification.save()

        # Check the updated status
        notification.refresh_from_db()
        self.assertTrue(notification.read)
