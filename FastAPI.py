from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, API world!"}

tasks = [
    {"id": 1, "title": "Learn Python", "done": False},
    {"id": 2, "title": "Build an API", "done": False}
]

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def add_task(task: dict):
    task["id"] = len(tasks) + 1
    tasks.append(task)
    return task

from pydantic import BaseModel
class Task(BaseModel):
    title: str
    done: bool = False

@app.post("/tasks")
def add_task(task: Task):
    task_dict = task.dict()
    task_dict["id"] = len(tasks) + 1
    tasks.append(task_dict)
    return task_dict

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = updated_task.title
            task["done"] = updated_task.done
            return task
    return {"error": "Task not found"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}
    return {"error": "Task not found"}

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()

@app.get("/secure-data")
def secure_data(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != "admin" or credentials.password != "password":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return {"message": "This is secured data"}

from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#postgresql://localhost:5433
DATABASE_URL = "sqlite:///./tasks.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class TaskModel(Base):

    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    done = Column(Boolean, default=False)

Base.metadata.create_all(bind=engine)