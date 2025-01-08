from contextlib import asynccontextmanager
from typing import Annotated

import uvicorn
from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager

from src.models.tasks_model import STaskAdd
from src.database.database import create_tables
from src.database.database import delete_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('База очищена')
    await create_tables()
    print('База готова к работе')
    yield
    print('Выключение')

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
    