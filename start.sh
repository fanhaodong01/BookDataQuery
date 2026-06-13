#!/usr/bin/env bash
cd "$(dirname "$0")" || exit 1
source venv/bin/activate
python manage.py collectstatic --noinput
python manage.py migrate
gunicorn bookquery.wsgi:application --bind 0.0.0.0:8000 --workers 2
