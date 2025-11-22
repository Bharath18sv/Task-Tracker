from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, Index, func
from database import Base # Base is also from sqlalchemy
from enum import Enum as PyEnum

class PriorityEnum(PyEnum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

class StatusEnum(PyEnum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"

# defining ORM class which extends Base class(represents database table)
class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False) #stores ~255 chars, nullable=False : similar to NOT NULL in sql
    description = Column(Text)
    priority = Column(Enum(PriorityEnum, native_enum=False))
    status = Column(Enum(StatusEnum, native_enum=False)) #all databases doesn't support enums so native_enum=False
    due_date = Column(DateTime)
    created_at = Column(DateTime, default=func.now()) #if not given, stores the current time using func.now()
    
    # Add indexes for priority and status, because these columns are heavily queried in our project
    __table_args__ = (
        Index('idx_priority', 'priority'),
        Index('idx_status', 'status'),
        Index("idx_title", "title")
    )