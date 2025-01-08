from typing import Optional

from sqlalchemy.orm import  Mapped, mapped_column

from src.database.db_models.base_model import Model


class TaskOrm(Model):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]
