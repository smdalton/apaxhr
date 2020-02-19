import os
import time
import sys

def postgres_message():
    print("*" * 80)
    print("*" +" "* 78 + "*\n")
    print("*" +" "* 78 + "*\n")
    print(' PostGres DB is currently dirty needs to be clean before deployment ')
    print("*" +" "* 78 + "*\n")
    print("*" +" "* 78 + "*\n")

def start_dev_server():
    # set env's
    os.environ['SQL_ENGINE'] = 'django.db.backends.postgresql_psycopg2'
    os.environ['SQL_NAME'] = 'postgres-dev'
    os.environ['DEV_POSTGRES']='TRUE'
    # os.environ['USE_S3'] = 'TRUE'
    os.environ['AWS_ACCESS_KEY_ID'] = 'AKIATWWKT35LU5ED5FDY'
    os.environ['AWS_SECRET_ACCESS_KEY'] = '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'
    os.environ['AWS_STORAGE_BUCKET_NAME'] = 'apaxhr-test'
    os.environ['DEV']='TRUE'

    os.system('echo Starting Dev server.')
    os.system('python3 manage.py dev_db')

    # os.system('exec gunicorn apaxhr.wsgi:application \
    #         --bind 0.0.0.0:8000\
    #         --workers 3')
    # Profiling
    # os.system('python3 -m cProfile manage.py collectstatic --no-input > profiled_collectstatic')
    # os.system(' python3 -m cProfile manage.py runserver > profiled_runserver')
    os.system('python3 manage.py runserver')

def start_prod_server():

    os.environ['USE_S3'] = 'TRUE'
    os.environ['AWS_ACCESS_KEY_ID'] = 'AKIATWWKT35LU5ED5FDY'
    os.environ['AWS_SECRET_ACCESS_KEY'] = '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'
    os.environ['AWS_STORAGE_BUCKET_NAME'] = 'apaxhr-test'
    os.system('echo Starting Prod server.')
    os.system('python3 manage.py makemigrations')
    os.system('python3 manage.py migrate')
    os.system('python3 manage.py collectstatic --no-input')
    time.sleep(1)

    os.system('exec gunicorn apaxhr.wsgi:application \
        --bind 0.0.0.0:8000\
        --workers 3')

def start_prod_demo_server():
    os.environ['DEV_POSTGRES']='TRUE'
    os.environ['USE_S3'] = 'TRUE'
    os.environ['AWS_ACCESS_KEY_ID'] = 'AKIATWWKT35LU5ED5FDY'
    os.environ['AWS_SECRET_ACCESS_KEY'] = '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'
    os.environ['AWS_STORAGE_BUCKET_NAME'] = 'apaxhr-test'
    os.environ['DEV']='TRUE'
    os.system('echo Starting Prod server.')
    os.system('python3 manage.py dev_db')

    #os.system('python3 manage.py collectstatic --no-input')
    time.sleep(1)

    os.system('exec gunicorn apaxhr.wsgi:application \
        --bind 0.0.0.0:8000\
        --workers 3')

def start_dev_rabbit():
    os.environ['REDIS']='True'
    print('bring up redis container')

    start_dev_server()
    pass

func_dict = {
    'dev': start_dev_server,
    'dev_redis': start_dev_rabbit,
    'prod': start_prod_server,
    'dev_rabbit': start_dev_rabbit,
    'prod_demo': start_prod_demo_server,
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