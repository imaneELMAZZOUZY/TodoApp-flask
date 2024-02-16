from flask import Flask
from pymongo import MongoClient

from flask_cors import CORS


from .config import config_by_name

from flask_pymongo import PyMongo

mongo = PyMongo()
cors = CORS()
    


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    mongo.init_app(app)
    cors.init_app(app)
    
   
    return app

