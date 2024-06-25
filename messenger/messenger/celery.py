from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Установка переменной окружения для настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'messenger.settings')

app = Celery('messenger')

# Загрузка настроек из Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическое обнаружение задач в приложениях
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
