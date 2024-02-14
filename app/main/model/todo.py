
from dataclasses import Field
from bson import ObjectId
from typing import List, Optional

from datetime import datetime



class Todo:
    id: Optional[ObjectId] 
    title:str
    description:str
    priority:str
    completed:bool
    date_added: Optional[datetime]

    def __init__(self, title: str, description: str, priority: str, completed: bool, date_added: Optional[datetime] = None,id: Optional[ObjectId] = None):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = completed
        self.date_added = date_added

    def __repr__(self):
        return f"Todo(id={self.id}, title='{self.title}', description='{self.description}', priority='{self.priority}', completed={self.completed}, date_added={self.date_added})"
    
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'completed': self.completed,
            'date_added': self.date_added.isoformat() if self.date_added else None
        }


