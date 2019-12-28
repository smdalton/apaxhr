import os
import time

def start_prod_server():
    os.system('echo Starting Prod server.')
    os.system('python3 manage.py makemigrations')
    os.system('python3 manage.py migrate')
    time.sleep(1)
    print("*"*100)
    print('\n*\n*\n* PostGres DB is currently dirty need to clean before deployment *\n*\n*\n*')
    os.system('exec gunicorn apaxhr.wsgi:application \
        --bind 0.0.0.0:8000\
        --workers 3')
    print("*" * 100)
    #os.system('python3 -W ignore manage.py runserver 0.0.0.0:8000')
    #os.system('pwd')

start_prod_server()


#
# os.system('exec gunicorn apaxhr.wsgi:application \
#     --bind 0.0.0.0:8000\
#     --workers 3')

#python manage.py makemigrations
#python manage.py migrate
##python manage.py collectstatic --no-input
#exec python manage.py runserver