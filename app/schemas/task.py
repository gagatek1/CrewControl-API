from typing import Optional
from pydantic import BaseModel

class CreateTask(BaseModel):
    name: str
    description: str

class AdminCreateTask(BaseModel):
    name: str
    description: str
    user_id: int

class UpdateTask(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    done: Optional[bool] = False