from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, Index, func
from database import Base
from enum import Enum as PyEnum

class PriorityEnum(PyEnum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

class StatusEnum(PyEnum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    priority = Column(Enum(PriorityEnum, native_enum=False))
    status = Column(Enum(StatusEnum, native_enum=False))
    due_date = Column(DateTime)
    created_at = Column(DateTime, default=func.now())
    
    # Add indexes
    __table_args__ = (
        Index('idx_priority', 'priority'),
        Index('idx_status', 'status'),
    )