from pydantic import BaseModel, EmailStr

class CreateUser(BaseModel):
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    role: str
    password: str