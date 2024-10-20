from pydantic import BaseModel, EmailStr

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