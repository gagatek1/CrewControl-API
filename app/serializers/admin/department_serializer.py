from pydantic import BaseModel

class DepartmentSerializer(BaseModel):
    id: int
    name: str