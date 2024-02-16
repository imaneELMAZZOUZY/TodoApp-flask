from flask_restx import Resource
from flask import request

from app.main.util.dto import TodoDto




from ..service.todo_service import *


api= TodoDto.api
_todo= TodoDto.todo



@api.route('/')
class TodoList(Resource):
    @api.doc('list_of_registered_todos')
    @api.marshal_list_with(_todo, envelope='data')
    def get(self):
        """List all registered todos"""
        todos = get_all_todos()
        return [todo.to_dict() for todo in todos]
    

    

    @api.response(201, 'Todo successfully created.')
    @api.doc('create a new todo')
    @api.expect(_todo, validate=True)
    def post(self):
        """Creates a new Todo """
        data = request.json        
        todo= save_new_todo(data=data)
        if not todo:
            return {
                'message': 'Error, try again'
            }, 400
        else:
            return todo.to_dict(), 201
    

@api.route('/<id>')
@api.param('id', 'The Todo identifier')
@api.response(404, 'Todo not found.')
class Todo(Resource):
    @api.doc('get a todo')
    @api.marshal_with(_todo)
    def get(self, id):
        """get a todo given its identifier"""
        todo = get_a_todo(id)
        if not todo:
            api.abort(404)
        else:
            return todo.to_dict()

    @api.doc('update a todo')
    @api.expect(_todo, validate=True)
    @api.marshal_with(_todo)
    def put(self, id):
        """update a todo given its identifier"""
        data = request.json
        updated_todo=update_a_todo(id, data)
        if not updated_todo:
            api.abort(404)
        else:
            return updated_todo.to_dict()

    @api.doc('delete a todo')
    def delete(self, id):
        """delete a todo given its identifier"""
        deleted = delete_a_todo(id)
        if deleted:
            return {
                'message': 'Deleted successfully'
            }, 200  
        else:
            return {
                'message': 'Error, try again'
            }, 400 
        

@api.route('/delete_all')
class DeleteAllTodoList(Resource):
    @api.doc('delete_all_todos')
    def delete(self):
        """Delete all todos"""
        deleted = delete_all_todos()
        if deleted:
            return {
                'message': 'Deleted successfully'
            }, 200  
        else:
            return {
                'message': 'Error, try again'
            }, 400 
        

@api.route('/completed')
class CompletedTodoList(Resource):
    @api.doc('list_of_completed_todos')
    @api.marshal_list_with(_todo, envelope='data')
    def get(self):
        """List all completed todos"""
        todos = get_all_completed_todos()
        return [todo.to_dict() for todo in todos]
    
    def delete(self):
        """Delete all completed todos"""
        deleted = delete_all_completed_todos()
        if deleted:
            return {
                'message': 'Deleted successfully'
            }, 200  
        else:
            return {
                'message': 'Error, try again'
            }, 400
    

@api.route('/uncompleted')
class UncompletedTodoList(Resource):
    @api.doc('list_of_uncompleted_todos')
    @api.marshal_list_with(_todo, envelope='data')
    def get(self):
        """List all uncompleted todos"""
        todos = get_all_uncompleted_todos()
        return [todo.to_dict() for todo in todos]





@api.route('/completed/<id>')
@api.param('id', 'The Todo identifier')
@api.response(404, 'Todo not found.')
class ChangeCompletedStatus(Resource):
    @api.response(201, 'Completed status changed successfully .')
    @api.doc('change completed todo status')
    @api.marshal_with(_todo)
    def put(self,id):
        """Change completed todo status"""
        todo= change_completed_status(id)
        if  not todo:
            api.abort(404)
        else :
            return todo.to_dict()


    





@api.route('/high_priority')
class HighPriorityTodoList(Resource):
    @api.doc('list_of_high_priority_todos')
    @api.marshal_list_with(_todo, envelope='data')
    def get(self):
        """List all high priority todos"""
        todos = get_all_high_priority_todos()
        return [todo.to_dict() for todo in todos]
    

@api.route('/medium_priority')
class MediumPriorityTodoList(Resource):
    @api.doc('list_of_medium_priority_todos')
    @api.marshal_list_with(_todo, envelope='data')
    def get(self):
        """List all medium priority todos"""
        todos = get_all_medium_priority_todos()
        return [todo.to_dict() for todo in todos]
    

@api.route('/low_priority')
class LowPriorityTodoList(Resource):
    @api.doc('list_of_low_priority_todos')
    @api.marshal_list_with(_todo, envelope='data')
    def get(self):
        """List all low priority todos"""
        todos = get_all_low_priority_todos()
        return [todo.to_dict() for todo in todos]
    


    



