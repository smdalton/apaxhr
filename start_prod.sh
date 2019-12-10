#!/bin/bash

echo Starting Gunicorn.

exec gunicorn apaxhr.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3