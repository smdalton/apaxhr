import os, sys
"""
Run tools help
"""
env_flags = ['DEV', 'DEV_REDIS', 'DEV_NGINX', 'DEV_REDIS_NGINX', 'PROD','SERVE_STATIC']

def clear_envs():
    for env in env_flags:
     try:
        os.environ.pop(env)
     except:
         print(env, "Not set")

# TODO: Run server with DEV sqlite db and no nginx or redis
def dev_no_services():
    clear_envs()
    os.environ['DEV']='True'
    os.environ['SERVE_STATIC']='True'
    os.chdir('app')
    os.system('python3 start_server.py dev')

def dev_on_docker():
    os.system('./devrun.sh')
# set envs
# TODO: Run server with DEV sqlite db and nginx
def dev_nginx():
    clear_envs()
# TODO: Run server with DEV sqlite db and redis
def dev_redis():
    clear_envs()
    #Todo bring up a system redis container
# TODO: Run server with DEV sqlite db redis, and nginx

def dev_redis_nginx():
    print("Running on nginx and redis")
# TODO:

def prod():
    print("running prod no services")

def prod_redis_nginx():
    print("Running prod on redis an nginx")

# TODO:
def kill_services():
    print("killing services")

function_dict ={
    'dev': dev_no_services,
    'dev_on_docker': dev_on_docker,
    'dev_nginx': dev_nginx,
    'dev_redis': dev_redis,
    'dev_redis_nginx': dev_redis_nginx,
    'prod_redis_nginx': prod_redis_nginx,
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
    print('Execute cleanp code here')
