from celery import shared_task
import logging
from django.apps import apps

logger = logging.getLogger(__name__)


@shared_task
def log_last_10_messages():
    # Использую get_model для загрузки модели Messages
    Messages = apps.get_model('drf_message_app', 'Messages', require_ready=False)
    last_10_messages = Messages.objects.order_by('-created_at')[:10]
    logger.info("Last 10 messages:")
    for message in last_10_messages:
        logger.info(f"{message.title}: {message.content}")
