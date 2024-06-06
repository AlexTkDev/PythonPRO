from django.contrib.auth.models import User
from django.db import models
from datetime import timedelta
from django.utils import timezone


class UserMessage(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="автор")
    message = models.TextField(blank=True, null=True, verbose_name="сообщение")
    date_sent = models.DateTimeField(auto_now_add=True, verbose_name="дата отправки")
    is_system_message = models.BooleanField(default=False, verbose_name="системное сообщение", blank=True)

    class Meta:
        verbose_name = "запись"
        verbose_name_plural = "записи"
        permissions = [
            ("give_access_to_chat", "give the user access to the chat"),
            ("give_access_to_delete_message", "give the user access to the delete message")
        ]

    def can_edit(self, user):
        return user.is_superuser or (self.author == user and timezone.now() - self.date_sent < timedelta(days=1))

    def can_delete(self, user):
        return user.is_superuser or (self.author == user and timezone.now() - self.date_sent < timedelta(days=1))

    @property
    def can_be_deleted(self):
        return timezone.now() - self.date_sent < timedelta(days=1)

    def __str__(self):
        return self.message if self.message else "Поле сообщение не заполнено"


class MessageLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    action = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class UserStatus(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="status")
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {'Online' if self.is_online else 'Offline'}"