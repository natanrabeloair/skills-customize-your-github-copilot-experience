# Starter code for the FastAPI REST API assignment

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Task(BaseModel):
    id: int
    title: str
    completed: bool = False


# Store tasks in memory for this assignment.
tasks = []


@app.get("/")
def welcome():
    # Return a short welcome message.
    pass


@app.post("/tasks", status_code=201)
def create_task(task: Task):
    # Add the task to the in-memory list and return it.
    pass


@app.get("/tasks")
def get_tasks():
    # Return all tasks.
    pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # Find the task by ID, or raise a 404 response if it does not exist.
    pass


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    # Update the task by ID, or raise a 404 response if it does not exist.
    pass


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    # Delete the task by ID, or raise a 404 response if it does not exist.
    pass
