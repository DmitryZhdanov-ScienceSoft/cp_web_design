#!/bin/sh
set -e

python manage.py migrate
python manage.py collectstatic --no-input
gunicorn web_design.wsgi:application --bind 0.0.0.0:8000