# pydantic model for defining data structures and validation rules

from pydantic import BaseModel, ConfigDict  # Updated for Pydantic v2
from datetime import datetime
from typing import Optional
from enum import Enum  # sets of choices

class PriorityEnum(str, Enum):  # Priority.LOW == "LOW"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

class StatusEnum(str, Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None  # None if not passed
    priority: PriorityEnum
    status: StatusEnum
    due_date: datetime

# for input data (when user creates the task)
class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    priority: Optional[PriorityEnum] = None
    status: Optional[StatusEnum] = None

# response model : includes task base and extra fields
class Task(TaskBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)  # Pydantic v2 syntax (replaces orm_mode)

class TaskInsights(BaseModel):
    total_tasks: int
    high_priority: int
    due_soon: int
    busiest_day: Optional[str] = None
    summary: str