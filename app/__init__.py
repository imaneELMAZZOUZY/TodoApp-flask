# app/__init__.py

from flask_restx import Api
from flask import Blueprint

from .main.controller.todo_controller import api as todo_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Todo App API',
          version='1.0'
          )

api.add_namespace(todo_ns, path='/todo')
