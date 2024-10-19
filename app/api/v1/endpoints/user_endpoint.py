from fastapi import APIRouter

from passlib.context import CryptContext

from starlette import status

from app.schema.user import CreateUser
from app.models.user import User
from app.core.database import db_dependency

user_router = APIRouter(prefix='/users')

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

@user_router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user: CreateUser):
    create_user_model = User(
        email=create_user.email,
        username=create_user.username,
        first_name=create_user.first_name,
        last_name=create_user.last_name,
        hashed_password=bcrypt_context.hash(create_user.password)
    )

    db.add(create_user_model)
    db.commit()

    return { 'status': 'created' }
