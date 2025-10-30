from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum

class PriorityEnum(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

class StatusEnum(str, Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    priority: PriorityEnum
    status: StatusEnum
    due_date: datetime

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    priority: Optional[PriorityEnum] = None
    status: Optional[StatusEnum] = None

class Task(TaskBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class TaskInsights(BaseModel):
    total_tasks: int
    high_priority: int
    due_soon: int
    busiest_day: Optional[str] = None
    summary: str