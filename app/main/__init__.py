from flask import Flask
from pymongo import MongoClient


from .config import config_by_name
from flask_pymongo import PyMongo

mongo = PyMongo()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    mongo.init_app(app)
    
   
    return app

