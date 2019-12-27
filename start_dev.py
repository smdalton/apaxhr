import os
import time

def start_dev_server():
    os.system('echo Starting dev server.')
    os.system('python3 manage.py dev_db')
    time.sleep(1)
    os.system('python3 -W ignore manage.py runserver 0.0.0.0:8000')
    os.system('pwd')


start_dev_server()


#
# os.system('exec gunicorn apaxhr.wsgi:application \
#     --bind 0.0.0.0:8000\
#     --workers 3')

#python manage.py makemigrations
#python manage.py migrate
##python manage.py collectstatic --no-input
#exec python manage.py runserver