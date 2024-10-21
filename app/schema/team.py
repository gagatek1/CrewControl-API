from pydantic import BaseModel

from typing import Optional

class CreateTeam(BaseModel):
    name: str
    department: str

class UpdateTeam(BaseModel):
    name: Optional[str] = None
    department: Optional[str] = None
    team_leader: Optional[int] = None