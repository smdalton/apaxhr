#!/bin/bash

echo Starting Gunicorn.
#python manage.py runserver localhost:8000

exec gunicorn apaxhr.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3