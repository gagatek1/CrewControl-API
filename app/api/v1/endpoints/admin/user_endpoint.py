from fastapi import APIRouter, Depends, HTTPException

from starlette import status

from typing import List

from app.core.database import db_dependency
from app.core.security import get_current_user
from app.models.user import User, UserRole
from app.schema.user import AdminUpdateUser
from app.services.admin.user.update_service import update_service
from app.services.admin.user.delete_service import delete_service
from app.serializers.admin.user_serializer import UserSerializer

user_router = APIRouter(prefix='/users')

@user_router.get('/', response_model=List[UserSerializer])
async def get_users(db: db_dependency, get_admin: dict = Depends(get_current_user)):
    current_admin = db.query(User).filter(User.id == get_admin['user_id']).first()

    if current_admin.role == UserRole.admin:
        users = db.query(User).all()

        return users
    else:
        raise HTTPException(status_code=401, detail='Could not validate')


@user_router.put('/update/{user_id}', response_model=UserSerializer)
async def update_user(user_id: int, db: db_dependency, update_user: AdminUpdateUser, get_admin: dict = Depends(get_current_user)):
    current_admin = db.query(User).filter(User.id == get_admin['user_id']).first()
    user = update_service(current_admin, user_id, update_user, db)

    return user
    

@user_router.delete('/delete/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: db_dependency, get_admin: dict = Depends(get_current_user)):
    current_admin = db.query(User).filter(User.id == get_admin['user_id']).first()
    
    delete_service(current_admin, user_id, db)