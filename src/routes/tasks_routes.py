from contextlib import asynccontextmanager
from typing import Annotated

import uvicorn
from fastapi import FastAPI, Depends

from src.database.engine.session_maker import lifespan
from src.schemas.tasks_model import STaskAdd


app = FastAPI(lifespan=lifespan)

tasks = []

@app.post('/tasks')
async def add_task(
        task: Annotated[STaskAdd, Depends()],
):
    tasks.append(task)
    return {'ok': True}

# @app.get('/tasks')
# def get_tasks():
#     task = Task(name='Запиши это видео')
#     return {'data': task}

if __name__ == '__main__':
    uvicorn.run('tasks_routes:app', reload=True)
    