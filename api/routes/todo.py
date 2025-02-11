from fastapi import APIRouter, HTTPException
from api.models.todo import Todo
from api.schemas.todo import GetTodo, PostTodo, PutTodo

todo_router = APIRouter(prefix='/api', tags=['Todo'])

# ------------------------ Get All Todos

@todo_router.get('/', response_model=list[GetTodo])
async def all_todos():
    todos = await GetTodo.from_queryset(Todo.all()) #understand this query further how is it working?
    return todos

# ------------------------ Create Todo

@todo_router.post('/', response_model=GetTodo)
async def post_todo(todo: PostTodo):
    new_todo = await Todo.create(**todo.model_dump(exclude_none=True)) 
    return await GetTodo.from_tortoise_orm(new_todo) #Converts it to GetTodo schema using from_tortoise_orm().

# ------------------------ Get Single Todo

@todo_router.get('/{id}', response_model=GetTodo)
async def get_todo(id: int):
    todo = await Todo.get_or_none(id=id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found!")
    return await GetTodo.from_tortoise_orm(todo)

# ------------------------ Update Todo

@todo_router.put('/{id}', response_model=GetTodo)
async def put_todo(id: int, todo: PutTodo):
    existing_todo = await Todo.filter(id=id).exists()
    if not existing_todo:
        raise HTTPException(status_code=404, detail="Todo not found!")
    await Todo.filter(id=id).update(**todo.model_dump(exclude_unset=True))
    return await GetTodo.from_tortoise_orm(await Todo.get(id=id))

# ------------------------ Delete Todo

@todo_router.delete('/{id}')
async def delete_todo(id: int):
    existing_todo = await Todo.filter(id=id).exists()
    if not existing_todo:
        raise HTTPException(status_code=404, detail="Todo not found!")
    existing_todo = await Todo.filter(id=id).delete()
    return {"message": "Todo deleted"}