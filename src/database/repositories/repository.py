from sqlalchemy import select

from src.database.db_models.tasks_orm_model import TaskOrm
from src.database.engine.session_maker import new_session
from src.schemas.tasks_model import STaskAdd, STask


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def get_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [STask.model_validate(task_model) for task_model in task_models]

            return task_schemas