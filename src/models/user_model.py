from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    age: int
    is_subscribed: bool

