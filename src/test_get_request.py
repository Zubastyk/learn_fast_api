from fastapi import FastAPI, Query

insighter_sender_app = FastAPI(description='sender_descrip')

@insighter_sender_app.get(path='/',
                          description='sender_descrip',
                          name='sender_name')
async def home():
    return {'Hello!': 'You just made a GET-request to the CODE-API'}

@insighter_sender_app.get('/new_data')
async def new_data():
    return {'Data': 'New_data'}