from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends

from typing import Annotated

from passlib.context import CryptContext

from starlette import status

from datetime import timedelta

from app.schema.user import CreateUser, UpdateUser
from app.models.user import User
from app.core.database import db_dependency
from app.core.security import create_access_token, get_current_user

user_router = APIRouter(prefix='/users', tags=['users'])

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def auth_user(username: str, password: str, db):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user

@user_router.get('/me')
async def get_me(db: db_dependency, get_user: dict = Depends(get_current_user)):
    user_id = get_user['user_id']
    user = db.query(User).filter(User.id == user_id).first()

    return user

@user_router.get('/{user_id}')
async def get_user(user_id: int, db: db_dependency):
    user = db.query(User).filter(User.id == user_id).first()

    return user


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

@user_router.put('/update/me', status_code=status.HTTP_202_ACCEPTED)
async def update_me(db: db_dependency, update_user: UpdateUser, get_user: dict = Depends(get_current_user)):
    user = db.query(User).filter(User.id == get_user['user_id']).first()

    if user is None:
        raise HTTPException(status=404, detail='User not found')
    
    user.email = update_user.email
    user.username = update_user.username
    user.hashed_password = bcrypt_context.hash(update_user.password)
    db.commit()
    db.refresh(user)

    return user

@user_router.post('/auth')
async def login_user(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    user = auth_user(form_data.username, form_data.password, db)

    if not user:
        raise HTTPException(status_code=401, detail='Could not validate user')
    else:
        return create_access_token(
            username=user.username,
            user_id=user.id,
            expires_delta=timedelta(days=2),
            db=db
            )
    

