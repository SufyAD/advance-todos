from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return({'status': 'ToDo app Created by Sufyan'})