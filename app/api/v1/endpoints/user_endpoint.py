from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from starlette import status

from app.core.database import db_dependency
from app.core.security import get_current_user
from app.models.user import User
from app.schema.user import CreateUser, JoinUser, UpdateUser
from app.services.user.create_service import create_service
from app.services.user.login_service import login_service
from app.services.user.update_service import update_service
from app.services.user.join_service import join_service
from app.serializers.user_serializer import UserSerializer

user_router = APIRouter(prefix='/users', tags=['users'])

@user_router.get('/me', response_model=UserSerializer)
async def get_me(db: db_dependency, get_user: dict = Depends(get_current_user)):
    user_id = get_user['user_id']
    user = db.query(User).filter(User.id == user_id).first()

    return user

@user_router.get('/{user_id}', response_model=UserSerializer)
async def get_user(user_id: int, db: db_dependency):
    user = db.query(User).filter(User.id == user_id).first()

    return user


@user_router.post('/create', status_code=status.HTTP_201_CREATED, response_model=UserSerializer)
async def create_user(db: db_dependency, create_user: CreateUser):
    user = create_service(db, create_user)

    return user

@user_router.put('/update/me', response_model=UserSerializer)
async def update_me(db: db_dependency, update_user: UpdateUser, get_user: dict = Depends(get_current_user)):
    user = update_service(update_user, get_user, db)

    return user

@user_router.post('/auth')
async def login_user(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    token = login_service(form_data.username, form_data.password, db)

    return token

@user_router.post('/join', response_model=UserSerializer)
async def join_team(db: db_dependency, join_user: JoinUser, get_user: dict = Depends(get_current_user)):
    user = join_service(get_user, join_user, db)

    return user
