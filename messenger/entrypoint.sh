#!/bin/sh

# Применение миграций
python manage.py migrate

# Запуск Celery
exec "$@"
