#!/bin/sh
echo 'Running migrations...'
python manage.py makemigrations products core users
python manage.py migrate

echo 'Collecting static files...'
python manage.py collectstatic --no-input

exec "$@"