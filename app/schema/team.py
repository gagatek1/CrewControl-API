from pydantic import BaseModel

class CreateTeam(BaseModel):
    name: str
    department: str