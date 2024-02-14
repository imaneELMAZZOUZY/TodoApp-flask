import os
from re import M


basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):

    DEBUG = True
    MONGO_URI = "mongodb://localhost:27017/todo_db_dev"
    
  


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    MONGO_URI = "mongodb://localhost:27017/todo_db_test"



class ProductionConfig(Config):
    DEBUG = False
    MONGO_URI = "mongodb://localhost:27017/todo_db_prod"



config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY