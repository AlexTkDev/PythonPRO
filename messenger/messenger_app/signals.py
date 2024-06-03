from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from .models import MessageLog, UserMessage
from django.contrib.auth.models import User


@receiver(pre_save, sender=UserMessage)
def log_send_message(sender, instance, **kwargs):
    if not instance.pk:
        instance.is_system_message = False
        action = f"{instance.author.username} отправил сообщение в чат"
        MessageLog.objects.create(user=instance.author, action=action)


@receiver(post_save, sender=UserMessage)
def create_superuser_notification(sender, instance, created, **kwargs):
    if created and instance.author.is_superuser:
        action = f"{instance.author.username} отправил сообщение суперюзеру"
        MessageLog.objects.create(user=instance.author, action=action)

