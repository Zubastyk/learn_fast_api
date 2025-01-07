from fastapi import FastAPI

from src.models.feedback_model import Feedback


app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Привет'}
# новый роут
@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}

@app.post('/feedback')
def create_feedback(feedback: Feedback):
    return feedback