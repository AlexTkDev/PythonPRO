FROM python:3.12-slim

# Установка зависимостей системы
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev

# Создание рабочей директории
WORKDIR /code

# Копирование зависимостей проекта и установка
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода проекта
COPY . /code/

# Установка точки входа
ENTRYPOINT ["./entrypoint.sh"]
