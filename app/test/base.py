from flask_testing import TestCase
from app.main import db
from manage import app
from flask_pymongo import PyMongo


mongo = PyMongo()

class BaseTestCase(TestCase):
    """ Base Tests """

    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')
        mongo.init_app(app)


        return app




