#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
# up one level

#python manage.py makemigrations
#python manage.py migrate


exec gunicorn apaxhr.wsgi:application \
    --bind 0.0.0.0:8000\
    --workers 3