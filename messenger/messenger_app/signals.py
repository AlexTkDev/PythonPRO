from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.contrib import messages
from django.contrib.auth.models import User
from .models import MessageLog, UserMessage, UserStatus
from django.contrib.auth.signals import user_logged_in, user_logged_out



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
        # Добавляем сообщение в сессию
        if hasattr(instance, 'request') and instance.request:
            messages.success(instance.request, 'Вы успешно отправили сообщение суперюзеру')


@receiver(user_logged_in)
def set_user_online(sender, user, request, **kwargs):
    status, created = UserStatus.objects.get_or_create(user=user)
    status.is_online = True
    status.save()


@receiver(user_logged_out)
def set_user_offline(sender, user, request, **kwargs):
    status, created = UserStatus.objects.get_or_create(user=user)
    status.is_online = False
    status.save()