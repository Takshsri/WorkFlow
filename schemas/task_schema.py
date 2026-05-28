from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime


class TaskCreate(BaseModel):

    title: str

    description: str

    priority: str

    assigned_to: int

    deadline: date


class TaskUpdate(BaseModel):

    title: Optional[str] = None

    description: Optional[str] = None

    priority: Optional[str] = None

    assigned_to: Optional[int] = None

    deadline: Optional[date] = None

    status: Optional[str] = None


class TaskOut(BaseModel):

    id: int

    title: str

    description: str

    status: str

    priority: str

    assigned_to: int

    created_by: int

    deadline: date

    created_at: datetime

    updated_at: datetime

    class Config:

        from_attributes = True