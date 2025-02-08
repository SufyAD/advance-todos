from fastapi import APIRouter

todo_router = APIRouter(prefix='/api', tags=['Todo'])

@todo_router.get('/')
def all_todos():
    return "Show all todos"

@todo_router.post('/')
def post_todo():
    return "Post todo called"

@todo_router.get('/{id}')
def get_todo(id: str):
    return "Get todo"

@todo_router.put('/{id}')
def put_todo(key):
    return "Update todo"


@todo_router.delete('/{id}')
def delete_todo(id: str):
    return "Delete todo"