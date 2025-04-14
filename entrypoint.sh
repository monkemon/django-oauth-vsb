#!/bin/sh

cd src/oauth2-django-vsb || exit 1
python manage.py collectstatic --noinput || exit 1
python -m gunicorn site_main.wsgi -b 0.0.0.0:$GUNICORN_PORT
