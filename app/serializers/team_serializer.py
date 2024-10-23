from pydantic import BaseModel

class TeamSerializer(BaseModel):
    id: int
    name: str
    department_id: int
    team_leader: int