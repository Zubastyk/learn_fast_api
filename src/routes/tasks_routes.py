import uvicorn
from fastapi import FastAPI

from src.models.tasks_model import Task_model

app = FastAPI()

@app.get('/tasks')
def get_tasks():
    task = Task_model(name='Запиши это видео')
    return {'data': task}

if '__name__' == '__main__':
    uvicorn.run('tasks_routes:app', reload=True)
    