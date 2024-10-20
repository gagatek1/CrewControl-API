from fastapi import APIRouter, HTTPException

from passlib.context import CryptContext

from starlette import status

from app.schema.user import CreateUser, UpdateUser
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

@user_router.put('/update/{user_id}', status_code=status.HTTP_202_ACCEPTED)
async def update_user(user_id: int, db: db_dependency, update_user: UpdateUser):
    db_user = db.query(User).filter(User.id == user_id).first()

    if db_user is None:
        raise HTTPException(status=404, detail='User not found')
    
    db_user.email = update_user.email
    db_user.username = update_user.username
    db_user.hashed_password = bcrypt_context.hash(update_user.password)
    db.commit()
    db.refresh(db_user)

    return db_user
    

