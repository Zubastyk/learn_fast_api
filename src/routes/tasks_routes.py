from typing import Annotated

from fastapi import Depends, APIRouter

from src.database.repositories.repository import TaskRepository
from src.schemas.tasks_model import STaskAdd


router = APIRouter(
    prefix='/tasks',
    tags=['Tasks'],
)


@router.post('')
async def add_task(
        task: Annotated[STaskAdd, Depends()],
):
    task_id = await TaskRepository.add_one(task)
    return {'ok': True, 'task_id': task_id}

@router.get('')
async def get_tasks():
    tasks = await TaskRepository.get_all()
    return {'tasks': tasks}


    