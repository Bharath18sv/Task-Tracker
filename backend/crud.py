from sqlalchemy.orm import Session
from models import Task, PriorityEnum, StatusEnum
from schemas import TaskCreate, TaskUpdate
from datetime import datetime, timedelta
from collections import Counter
from typing import List, Optional

def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

def get_tasks(db: Session, skip: int = 0, limit: int = 100, status: Optional[StatusEnum] = None, priority: Optional[PriorityEnum] = None, sort_by_due_date: bool = False):
    query = db.query(Task)
    
    if status:
        query = query.filter(Task.status == status)
    
    if priority:
        query = query.filter(Task.priority == priority)
        
    if sort_by_due_date:
        query = query.order_by(Task.due_date)
        
    return query.offset(skip).limit(limit).all()

def create_task(db: Session, task: TaskCreate):
    db_task = Task(
        title=task.title,
        description=task.description,
        priority=task.priority,
        status=task.status,
        due_date=task.due_date
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, task_update: TaskUpdate):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task:
        if task_update.priority is not None:
            db_task.priority = task_update.priority
        if task_update.status is not None:
            db_task.status = task_update.status
        db.commit()
        db.refresh(db_task)
        return db_task
    return None

def get_task_insights(db: Session):
    # Get all tasks
    tasks = db.query(Task).all()
    
    # Calculate insights
    total_tasks = len(tasks)
    high_priority_count = len([t for t in tasks if t.priority == PriorityEnum.HIGH])
    
    # Tasks due within 3 days
    now = datetime.now()
    three_days_later = now + timedelta(days=3)
    due_soon_count = len([t for t in tasks if t.due_date and now <= t.due_date <= three_days_later])
    
    # Busiest day calculation
    busiest_day = None
    if tasks:
        # Count tasks by due date (date part only)
        date_counts = Counter()
        for task in tasks:
            if task.due_date:
                date_str = task.due_date.date().isoformat()
                date_counts[date_str] += 1
        
        if date_counts:
            busiest_day = date_counts.most_common(1)[0][0] if date_counts else None
    
    # Generate summary
    summary = f"You have {total_tasks} tasks"
    if total_tasks > 0:
        summary += f" — {high_priority_count} are High priority"
        if due_soon_count > 0:
            summary += f" and {due_soon_count} due soon"
        summary += "."
    else:
        summary += "."
    
    return {
        "total_tasks": total_tasks,
        "high_priority": high_priority_count,
        "due_soon": due_soon_count,
        "busiest_day": busiest_day,
        "summary": summary
    }