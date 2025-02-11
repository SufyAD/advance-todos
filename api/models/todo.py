from tortoise.models import Model
from tortoise.fields import IntField, BooleanField, CharField

#here we have created a database model for out Todo
class Todo(Model):
    id = IntField(primary_key=True)
    task = CharField(max_length=100, null=False)
    done = BooleanField(default=False)