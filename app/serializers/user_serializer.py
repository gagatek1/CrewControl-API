from pydantic import BaseModel, EmailStr

from typing import Optional

class UserSerializer(BaseModel):
    id: int
    email: EmailStr
    username: str
    first_name: str
    last_name: str
    team_id: Optional[int]