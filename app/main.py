from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from api.routes.todo import todo_router

app = FastAPI()
app.include_router(todo_router)

# ----------- register tortoise DB
register_tortoise(
    app=app,
    db_url="sqlite://db.sqlite3",  # Change this for PostgreSQL, MySQL, etc.
    modules={"models": ["models.todo"]},  # Ensure this matches your models path
    generate_schemas=True,  # Auto-generate DB schema
    add_exception_handlers=True,  # Handles database errors
)

@app.get('/')
def index():
    return({'status': 'ToDo app Created by Sufyan'})

