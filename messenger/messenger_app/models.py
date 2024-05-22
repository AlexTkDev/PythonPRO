from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class UserMessage(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="автор")
    message = models.TextField(blank=True, null=True, verbose_name="сообщение")
    date_sent = models.DateTimeField(auto_now_add=True, verbose_name="дата отправки")

    class Meta:
        verbose_name = "запись"
        verbose_name_plural = "записи"

    def __str__(self):
        return self.message if self.message else "Поле сообщение не заполнено"
