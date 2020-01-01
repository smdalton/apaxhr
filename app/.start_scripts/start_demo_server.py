import os
import time

def start_prod_server():
    # go up one level
    os.system('..')
    os.system('echo Starting test server.')
    os.system('python manage.py dev_db')
    os.system('python3 manage.py makemigrations')
    os.system('python3 manage.py migrate')
    # Execute tests here

    time.sleep(1)
    os.system()
    os.system('python3 -W ignore manage.py runserver 0.0.0.0:8000')
    os.system('pwd')

start_prod_server()


#
# os.system('exec gunicorn apaxhr.wsgi:application \
#     --bind 0.0.0.0:8000\
#     --workers 3')

#python manage.py makemigrations
#python manage.py migrate
##python manage.py collectstatic --no-input
#exec python manage.py runserver