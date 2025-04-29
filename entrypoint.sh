#!/bin/bash

echo " Creating migrations..."
python manage.py makemigrations --noinput

echo " Applying migrations..."
python manage.py migrate --noinput

echo " Collecting static files..."
python manage.py collectstatic --noinput

echo " Starting Gunicorn..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
