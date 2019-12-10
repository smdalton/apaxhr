#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
# up one level

exec gunicorn apaxhr.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3