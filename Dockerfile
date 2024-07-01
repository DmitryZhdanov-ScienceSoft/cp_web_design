FROM python:3.11-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "web_design.wsgi:application", "--bind", "0.0.0.0:8000"]
