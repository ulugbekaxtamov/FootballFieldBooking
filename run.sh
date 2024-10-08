#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
#python manage.py makemigrations
python manage.py migrate

# Start server
echo "Starting server"
#python manage.py runserver 0.0.0.0:8000
#daphne -b 0.0.0.0 -p 8000 wsgi.asgi:application
gunicorn --bind 0.0.0.0:8000 --workers 2 config.wsgi
