from pydantic import BaseModel

class CreateTask(BaseModel):
    name: str
    description: str

class UpdateTask(BaseModel):
    name: str
    description: str
    done: bool