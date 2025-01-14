
import uvicorn
from fastapi import FastAPI

from src.database.engine.session_maker import lifespan
from src.routes.tasks_routes import router as tasks_routes



app = FastAPI(lifespan=lifespan)
app.include_router(tasks_routes)



if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, host="0.0.0.0", port=83)
