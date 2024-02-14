from datetime import datetime
from bson import ObjectId
from pymongo import ReturnDocument

from ..model.todo import Todo
from dateutil.parser import parse

from app.main import mongo

def save_new_todo(data):
    todos = mongo.db.todos

    new_todo = Todo(
        title=data["title"],
        description=data.get("description", ""),  
        priority=data.get("priority", ""), 
        completed=False, 
        date_added=datetime.utcnow()
    )

    inserted_todo = todos.insert_one(new_todo.to_dict())
    new_todo.id = inserted_todo.inserted_id

    return new_todo.id

def get_all_todos():
    todos = mongo.db.todos
    return [
        Todo(
            id=todo["_id"],
            title=todo["title"],
            description=todo.get("description", ""),  
            priority=todo.get("priority", ""), 
            completed=todo.get("completed", False), 
            date_added=parse(todo.get("date_added"))
        ) 
        for todo in todos.find()
    ]

def get_a_todo(id):
    todos = mongo.db.todos
    todo = todos.find_one({"_id": ObjectId(id)})
    return Todo(
        id=todo["_id"],
        title=todo["title"],
        description=todo.get("description", ""),  
        priority=todo.get("priority", ""), 
        completed=todo.get("completed", False), 
        date_added=parse(todo.get("date_added"))
    ) if todo else None


def get_all_completed_todos():
    todos = mongo.db.todos
    return [
        Todo(
            id=todo["_id"],
            title=todo["title"],
            description=todo.get("description", ""),  
            priority=todo.get("priority", ""), 
            completed=todo.get("completed", False), 
            date_added=parse(todo.get("date_added"))
        ) 
        for todo in todos.find({"completed": True})
    ]



def get_all_uncompleted_todos():
    todos = mongo.db.todos
    return [
        Todo(
            id=todo["_id"],
            title=todo["title"],
            description=todo.get("description", ""),  
            priority=todo.get("priority", ""), 
            completed=todo.get("completed", False), 
            date_added=parse(todo.get("date_added"))
        ) 
        for todo in todos.find({"completed": False})
    ]

def get_all_high_priority_todos():
    todos = mongo.db.todos
    return [
        Todo(
            id=todo["_id"],
            title=todo["title"],
            description=todo.get("description", ""),  
            priority=todo.get("priority", ""), 
            completed=todo.get("completed", False), 
            date_added=parse(todo.get("date_added"))
        ) 
        for todo in todos.find({"priority": "high"})
    ]

def get_all_medium_priority_todos():
    todos = mongo.db.todos
    return [
        Todo(
            id=todo["_id"],
            title=todo["title"],
            description=todo.get("description", ""),  
            priority=todo.get("priority", ""), 
            completed=todo.get("completed", False), 
            date_added=parse(todo.get("date_added"))
        ) 
        for todo in todos.find({"priority": "medium"})
    ]

def get_all_low_priority_todos():
    todos = mongo.db.todos
    return [
        Todo(
            id=todo["_id"],
            title=todo["title"],
            description=todo.get("description", ""),  
            priority=todo.get("priority", ""), 
            completed=todo.get("completed", False), 
            date_added=parse(todo.get("date_added"))
        ) 
        for todo in todos.find({"priority": "low"})
    ]

def update_a_todo(id, data):
    todos = mongo.db.todos
    todo = todos.find_one({"_id": ObjectId(id)})
    
    if not todo:
        return None
    
    updated_data = {
        "title": data.get("title", todo["title"]),
        "description": data.get("description", todo.get("description", "")),
        "priority": data.get("priority", todo.get("priority", "")),
        "completed": data.get("completed", todo.get("completed", False))
    }
    
    updated_doc = todos.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": updated_data},
        return_document=ReturnDocument.AFTER
        )
    
    
    if updated_doc:
        return Todo(
            id=updated_doc["_id"],
            title=updated_doc["title"],
            description=updated_doc.get("description", ""),  
            priority=updated_doc.get("priority", ""), 
            completed=updated_doc.get("completed", False), 
            date_added=parse(updated_doc.get("date_added"))
        )
    else:
        return None

def mark_as_completed(id):
    todos = mongo.db.todos
    todo = todos.find_one({"_id": ObjectId(id)})
    if not todo:
        return None
    todo['completed'] = True
    updated_doc = todos.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": todo},
        return_document=ReturnDocument.AFTER
    )
    return Todo(
        id=updated_doc["_id"],
        title=updated_doc["title"],
        description=updated_doc.get("description", ""),  
        priority=updated_doc.get("priority", ""), 
        completed=updated_doc.get("completed", False), 
        date_added=parse(updated_doc.get("date_added"))
    ) if updated_doc else None

def delete_a_todo(id):
    todos = mongo.db.todos
    result= todos.delete_one({"_id": ObjectId(id)})
    return result.deleted_count > 0

def delete_all_todos():
    todos = mongo.db.todos
    return todos.delete_many({}).__str__

def delete_all_completed_todos():
    todos = mongo.db.todos
    return todos.delete_many({"completed": True}).__str__


