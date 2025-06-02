from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from typing import List
from app.schemas.task_schema import TaskCreate, TaskOut, TaskUpdate
from app.services.task_service import create_task, get_tasks, get_task, update_task, delete_task
from app.services.auth_service import get_current_user

task_router = APIRouter(prefix="/tasks", tags=["Tasks"])

# Simulate email in background
def send_confirmation_email(email: str, title: str):
    print(f"Simulated email: Task '{title}' created for user {email}")

@task_router.post("/", response_model=TaskOut)
async def create_task_route(task: TaskCreate, background_tasks: BackgroundTasks, user=Depends(get_current_user)):
    task_obj = await create_task(str(user["_id"]), task)
    background_tasks.add_task(send_confirmation_email, user["email"], task.title)
    return TaskOut(
        id=str(task_obj["_id"]),
        title=task_obj["title"],
        description=task_obj["description"],
        status=task_obj["status"],
        due_date=task_obj["due_date"],
        created_at=task_obj["created_at"]
    )

@task_router.get("/", response_model=List[TaskOut])
async def list_tasks(user=Depends(get_current_user)):
    tasks = await get_tasks(str(user["_id"]))
    return [
        TaskOut(
            id=str(task["_id"]),
            title=task["title"],
            description=task["description"],
            status=task["status"],
            due_date=task["due_date"],
            created_at=task["created_at"]
        ) for task in tasks
    ]

@task_router.get("/{task_id}", response_model=TaskOut)
async def get_task_route(task_id: str, user=Depends(get_current_user)):
    task = await get_task(str(user["_id"]), task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return TaskOut(
        id=str(task["_id"]),
        title=task["title"],
        description=task["description"],
        status=task["status"],
        due_date=task["due_date"],
        created_at=task["created_at"]
    )

@task_router.put("/{task_id}", response_model=TaskOut)
async def update_task_route(task_id: str, update: TaskUpdate, user=Depends(get_current_user)):
    updated_task = await update_task(str(user["_id"]), task_id, update)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return TaskOut(
        id=str(updated_task["_id"]),
        title=updated_task["title"],
        description=updated_task["description"],
        status=updated_task["status"],
        due_date=updated_task["due_date"],
        created_at=updated_task["created_at"]
    )

@task_router.delete("/{task_id}")
async def delete_task_route(task_id: str, user=Depends(get_current_user)):
    await delete_task(str(user["_id"]), task_id)
    return {"detail": "Task deleted"}
