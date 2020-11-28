#!/bin/sh
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py create_users_and_documents
python3 manage.py create_positions
python3 manage.py create_centers
python3 manage.py create_permissions
python3 manage.py runserver 0.0.0.0:8014
