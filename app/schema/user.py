from pydantic import BaseModel, EmailStr

from app.models.user import UserRole

class CreateUser(BaseModel):
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    password: str

class UpdateUser(BaseModel):
    username: str
    email: EmailStr
    password: str

class AdminUpdateUser(BaseModel):
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    role: UserRole

class JoinUser(BaseModel):
    team_id: int