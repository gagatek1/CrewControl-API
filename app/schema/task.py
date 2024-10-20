from typing import Optional
from pydantic import BaseModel

class CreateTask(BaseModel):
    name: str
    description: str

class UpdateTask(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    done: Optional[bool] = None