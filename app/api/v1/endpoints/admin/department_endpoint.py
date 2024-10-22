from fastapi import APIRouter, Depends

from starlette import status

from app.core.database import db_dependency
from app.core.security import get_current_user
from app.models.user import User
from app.schema.department import Department
from app.services.admin.department.create_service import create_service
from app.services.admin.department.update_service import update_service
from app.services.admin.department.delete_service import delete_service

department_router = APIRouter(prefix='/departments')

@department_router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_department(create_department: Department, db: db_dependency, get_admin: dict = Depends(get_current_user)):
    current_admin = db.query(User).filter(User.id == get_admin['user_id']).first()
    department = create_service(current_admin, create_department, db)

    return department

@department_router.put('/update/{department_id}')
async def update_department(department_id, update_department: Department, db: db_dependency, get_admin: dict = Depends(get_current_user)):
    current_admin = db.query(User).filter(User.id == get_admin['user_id']).first()
    department = update_service(current_admin, department_id, update_department, db)

    return department

@department_router.delete('/delete/{department_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_department(department_id, db: db_dependency, get_admin: dict = Depends(get_current_user)):
    current_admin = db.query(User).filter(User.id == get_admin['user_id']).first()

    delete_service(current_admin, department_id, db)
