from pydantic import BaseModel, EmailStr

from typing import Optional

from app.models.user import UserRole

class UserSerializer(BaseModel):
    id: int
    email: EmailStr
    username: str
    first_name: str
    last_name: str
    role: UserRole
    team_id: Optional[int]