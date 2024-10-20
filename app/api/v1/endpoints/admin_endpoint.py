from fastapi import APIRouter, Depends, HTTPException

from app.core.database import db_dependency
from app.core.security import get_current_user
from app.models.user import User, UserRole
from app.schema.user import AdminUpdateUser

admin_router = APIRouter(prefix='/admin', tags=['admin'])

@admin_router.put('/update/{user_id}')
async def update_user(user_id: int, db: db_dependency, update_user: AdminUpdateUser, get_admin: dict = Depends(get_current_user)):
    current_admin = db.query(User).filter(User.id == get_admin['user_id']).first()
    user = db.query(User).filter(User.id == user_id).first()

    if current_admin.role == UserRole.admin:
        user.email = update_user.email
        user.username = update_user.username
        user.first_name = update_user.first_name
        user.last_name = update_user.last_name
        user.role = update_user.role

        db.commit()
        db.refresh(user)

        return user
    else:
        raise HTTPException(status_code=401, detail='Could not validate')

@admin_router.delete('/delete/{user_id}')
async def delete_user(user_id: int, db: db_dependency, get_admin: dict = Depends(get_current_user)):
    current_admin = db.query(User).filter(User.id == get_admin['user_id']).first()
    user = db.query(User).filter(User.id == user_id).first()

    if current_admin.role == UserRole.admin:
        if not user:
            raise HTTPException(status_code=404, detail='Could not find user')
        db.delete(user)
        db.commit()

        return { 'status': 'deleted' }
    else:
        raise HTTPException(status_code=401, detail='Could not validate')
    