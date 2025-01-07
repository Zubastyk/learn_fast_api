from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    num1: int
    num2: int

app = FastAPI()

@app.post('/calculate')
async def give_item(item: Item):
    result = item.num1 + item.num2
    return {'result': result}