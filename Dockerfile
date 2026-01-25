FROM python:3.12-slim

# Python-настройки
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Системные зависимости
# gcc + libpq нужны для psycopg2
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Установка зависимостей
COPY req.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r req.txt

# Копируем приложение
COPY app ./app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
