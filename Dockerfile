FROM python:3.11-slim

# Устанавливаем системные зависимости + netcat для ожидания БД
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "task_manager.wsgi:application", "--bind", "0.0.0.0:8000"]