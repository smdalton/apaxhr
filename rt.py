import os, sys
"""
Run tools help
"""
env_flags = ['DEV', 'DEV_REDIS', 'DEV_NGINX', 'DEV_REDIS_NGINX', 'PROD','SERVE_STATIC', 'USE_S3']

def clear_envs():
    for env in env_flags:
     try:
        os.environ.pop(env)
     except:
         print(env, "Not set")

# TODO: Run server with DEV sqlite db and no server_nginx or redis
def dev_no_services():
    clear_envs()
    os.chdir('app')
    os.system('python3 start_server.py dev')


def dev_on_docker():
    os.system('docker-compose -f docker-compose.dev.yml build')
    os.system('docker-compose -f docker-compose.dev.yml up')

# set envs

# TODO: Run server with DEV sqlite db and server_nginx
def dev_nginx():
    clear_envs()

# TODO: Run server with DEV sqlite db and redis
def dev_redis():
    clear_envs()
    #Todo bring up a system redis container
# TODO: Run server with DEV sqlite db redis, and server_nginx


def prod():
    print("running prod no services")

# TODO:
def kill_services():
    print("killing services")

function_dict ={
    'dev': dev_no_services,
    'dev_on_docker': dev_on_docker,
    'dev_redis': dev_redis,
    'prod_no_services': prod
}

try:
    option = sys.argv[1]
    print(f"Running {option}")
    function_dict[option]()
except:
    print([key for key in function_dict.keys()])
finally:
    kill_services()
    print('Execute cleanup code here')
