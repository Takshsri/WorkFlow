from users import User
from tasks import Task
from fastapi import FastAPI
from models.model import Base
from database import engine
from routes.user_routes import router
from routes.task_routes import router as task_router

app = FastAPI()
app.include_router(router)
app.include_router(task_router)
Base.metadata.create_all(bind=engine)
@app.get("/")
def home():
    return {"message": "Welcome to the Workflow Management System!"}

