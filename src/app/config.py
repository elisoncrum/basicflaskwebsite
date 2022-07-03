import os
import urllib
import json

def decode_env(env):
    _env = {}
    for k, v in env.items():
        if type(v) == int:
            _env[k] = v
        elif type(v) == str:
            try:
                _env[k] = json.loads(v)
            except:
                _env[k] = str(v)
    return _env

class Config(object):
    TEMPLATES_AUTO_RELOAD = True
    APP_DIRECTORY = os.getcwd() + "/app"
    TESTING = False

class Testing(Config):
    TEMPLATES_AUTO_RELOAD = True
    TESTING = True
    HOST = "localhost"
    PORT = 8000
    LOCAL_ENV = decode_env(os.environ)

    CLIENT_ID = "my_client_id"
    CLIENT_SECRET = "my_client_secret"

    DATABASE_HOST = "localhost"
    DATABASE_USERNAME = "admin"
    DATABASE_PASSWORD = "testing"
    DATABASE_NAME = "testing"
    DATABASE_URI = f"mysql+pymysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:3306/{DATABASE_NAME}"