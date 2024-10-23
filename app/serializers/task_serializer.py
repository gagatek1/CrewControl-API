from pydantic import BaseModel

class TaskSerializer(BaseModel):
    id: int
    name: str
    description: str
    done: bool