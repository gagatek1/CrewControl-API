from pydantic import BaseModel

from typing import Optional

class CreateTeam(BaseModel):
    name: str
    department_id: int

class UpdateTeam(BaseModel):
    name: Optional[str] = None
    department_id: Optional[int] = None
    team_leader: Optional[int] = None