from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1)
    description: Optional[str] = None
    status: str = Field(default="pending")
    due_date: datetime

class TaskOut(BaseModel):
    id: str
    title: str
    description: Optional[str]
    status: str
    due_date: datetime
    created_at: datetime

class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[str]
    due_date: Optional[datetime]
