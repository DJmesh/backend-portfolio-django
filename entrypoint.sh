#!/bin/bash

echo "Making migrations..."
python manage.py makemigrations users
python manage.py makemigrations activity_log
python manage.py makemigrations support_requests

echo "Applying migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
