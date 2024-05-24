from django.contrib.auth.models import User
from django.db import models
from datetime import timedelta
from django.utils import timezone


# Create your models here.


class UserMessage(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="автор")
    message = models.TextField(blank=True, null=True, verbose_name="сообщение")
    date_sent = models.DateTimeField(auto_now_add=True, verbose_name="дата отправки")

    class Meta:
        verbose_name = "запись"
        verbose_name_plural = "записи"
        permissions = [
            ("give_access_to_chat", "give the user access to the chat"),
            ("give_access_to_delete_message", "give the user access to the delete message")
        ]

    def can_edit(self, user):
        return self.author == user and timezone.now() - self.date_sent < timedelta(days=1)

    def can_delete(self, user):
        return user.is_superuser or (self.author == user and timezone.now() - self.date_sent < timedelta(days=1))

    @property
    def can_be_deleted(self):
        return timezone.now() - self.date_sent < timedelta(days=1)

    def __str__(self):
        return self.message if self.message else "Поле сообщение не заполнено"
