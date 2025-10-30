from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import get_db
from crud import get_tasks, create_task, update_task, get_task, get_task_insights
from schemas import Task, TaskCreate, TaskUpdate, TaskInsights
from models import StatusEnum, PriorityEnum

router = APIRouter()

@router.post("/tasks", response_model=Task)
def create_new_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db=db, task=task)

@router.get("/tasks", response_model=List[Task])
def read_tasks(
    status: Optional[StatusEnum] = None,
    priority: Optional[PriorityEnum] = None,
    sort: Optional[str] = None,
    db: Session = Depends(get_db)
):
    sort_by_due_date = sort == "due_date"
    tasks = get_tasks(db, status=status, priority=priority, sort_by_due_date=sort_by_due_date)
    return tasks

@router.patch("/tasks/{task_id}", response_model=Task)
def update_task_endpoint(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db)):
    db_task = update_task(db, task_id=task_id, task_update=task_update)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.get("/insights", response_model=TaskInsights)
def read_insights(db: Session = Depends(get_db)):
    return get_task_insights(db)