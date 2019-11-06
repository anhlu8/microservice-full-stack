from db.models.todoModel import TodoModel
from marshmallow_sqlalchemy import ModelSchema

class TodoSchema(ModelSchema):
    class Meta:
        model = TodoModel
        
OneTodoSchema = TodoSchema(many=False)
ManyTodoSchema = TodoSchema(many=True)