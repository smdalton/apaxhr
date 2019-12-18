import os

os.system('echo Starting dev server.')
os.system('python3 manage.py runserver')
#
# os.system('exec gunicorn apaxhr.wsgi:application \
#     --bind 0.0.0.0:8000\
#     --workers 3')

#python manage.py makemigrations
#python manage.py migrate
##python manage.py collectstatic --no-input
#exec python manage.py runserver