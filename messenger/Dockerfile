FROM python:3.12-slim

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Установка рабочей директории
WORKDIR /code

# Копирование зависимостей проекта и установка
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода проекта
COPY . /code/

# Копирование точки входа
COPY entrypoint.sh /code/
RUN chmod +x /code/entrypoint.sh

# Установка точки входа
ENTRYPOINT ["/code/entrypoint.sh"]

# Команда по умолчанию
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "messenger.wsgi:application"]
