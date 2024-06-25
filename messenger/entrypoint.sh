#!/bin/sh

# Применение миграций
echo "Применение миграций..."
python manage.py makemigrations
python manage.py migrate

# Запуск сервера
echo "Запуск сервера..."
exec "$@"
