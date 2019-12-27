#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
# up one level

#python manage.py makemigrations
#python manage.py migrate
##python manage.py collectstatic --no-input
#exec python manage.py runserver


gunicorn apaxhr.wsgi:application \
    --bind 0.0.0.0\
    --workers 3