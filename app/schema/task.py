from pydantic import BaseModel

class CreateTask(BaseModel):
    name: str
    description: str