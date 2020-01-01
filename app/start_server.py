import os
import time
import sys

def start_dev_server():
    # wipe and init the db
    os.environ['SERVE_STATIC1']='True'
    os.environ['DEV']='True'
    os.system('echo Starting dev server.')
    print(os.getcwd())
    os.system('python3 manage.py dev_db')
    os.system('python3 -W ignore manage.py runserver 0.0.0.0:8000')


# def start_demo_server():
#     os.system('echo Starting test server.')
#     os.system('python manage.py dev_db')
#     os.system('python3 manage.py makemigrations')
#     os.system('python3 manage.py migrate')
#     # Execute tests here
#     time.sleep(1)
#     os.system('python3 -W ignore manage.py runserver 0.0.0.0:8000')



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

def start_dev_redis():
    os.environ['REDIS']='True'
    print('bring up redis container')

    start_dev_server()
    pass

def start_dev_nginx():
    pass

def start_dev_redis_nginx():
    pass

func_dict = {
    'dev': start_dev_server,
    'dev_redis': start_dev_redis,
    'dev_nginx':start_dev_nginx,
    'dev_redis_nginx': start_dev_nginx,
    # 'demo': start_demo_server,
    'prod': start_prod_server,
}


option = sys.argv[1]
valid_options = ['dev','prod','demo']
try:
    assert(option in valid_options)
except:
    print(f"argument not provided / not in valid options: {valid_options} ")

func_dict[option]()




#

# os.system('exec gunicorn apaxhr.wsgi:application \
#     --bind 0.0.0.0:8000\
#     --workers 3')

#python manage.py makemigrations
#python manage.py migrate
##python manage.py collectstatic --no-input
#exec python manage.py runserver