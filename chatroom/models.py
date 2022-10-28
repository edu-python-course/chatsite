"""
Chatroom application models

"""

from django.db import models


class ChatRoomMessageModel(models.Model):
    """Chat room message model implementation"""

    class Meta:
        db_table = "message"
        verbose_name = "message"
        verbose_name_plural = "messages"
        ordering = "-created_at",

    created_at = models.DateTimeField(auto_now_add=True)
    group_name = models.CharField(max_length=32)
    message = models.TextField()

    def __repr__(self) -> str:
        """Return a string representation of an instance"""

        return (f"<ChatRoomMessageModel("
                f"created_at={self.created_at}, "
                f"group_name={self.group_name}, "
                f"message={self.message}"
                f")>")

    def __str__(self) -> str:
        """Return a string version of an instance"""

        return self.message
