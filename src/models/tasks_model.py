from typing import Optional

from pydantic import BaseModel


class Task_model(BaseModel):
    name: str
    description: Optional[str] = None
