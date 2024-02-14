from flask_restx import Namespace, fields




class TodoDto:
    api = Namespace('todo', description='todo related operations')
    todo = api.model('todo', {
        'id': fields.String( required=False ,description='todo identifier'),
        'title': fields.String(required=False, description='todo title'),
        'description': fields.String(required=False, description='todo description'),
        'priority': fields.String(required=False, description='todo priority'),
        'completed': fields.Boolean(required=False, description='todo completed'),
        'date_added': fields.DateTime(required=False, description='date added')
    })