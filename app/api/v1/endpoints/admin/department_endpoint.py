from fastapi import APIRouter, Depends, HTTPException

from starlette import status

from typing import List

from app.core.database import db_dependency
from app.core.security import get_current_user
from app.models.user import User, UserRole
from app.models.department import Department as DepartmentModel
from app.schema.department import Department 
from app.services.admin.department.create_service import create_service
from app.services.admin.department.update_service import update_service
from app.services.admin.department.delete_service import delete_service
from app.serializers.admin.department_serializer import DepartmentSerializer

department_router = APIRouter(prefix='/departments')

@department_router.post('/create', status_code=status.HTTP_201_CREATED, response_model=DepartmentSerializer)
async def create_department(create_department: Department, db: db_dependency, get_admin: dict = Depends(get_current_user)):
    current_admin = db.query(User).filter(User.id == get_admin['user_id']).first()
    department = create_service(current_admin, create_department, db)

    return department

@department_router.put('/update/{department_id}', response_model=DepartmentSerializer)
async def update_department(department_id, update_department: Department, db: db_dependency, get_admin: dict = Depends(get_current_user)):
    current_admin = db.query(User).filter(User.id == get_admin['user_id']).first()
    department = update_service(current_admin, department_id, update_department, db)

    return department

@department_router.delete('/delete/{department_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_department(department_id, db: db_dependency, get_admin: dict = Depends(get_current_user)):
    current_admin = db.query(User).filter(User.id == get_admin['user_id']).first()

    delete_service(current_admin, department_id, db)

@department_router.get('/', response_model=List[DepartmentSerializer])
async def show_departments(db: db_dependency, get_admin: dict = Depends(get_current_user)):
    current_admin = db.query(User).filter(User.id == get_admin['user_id']).first()

    if current_admin.role == UserRole.admin:
        departments = db.query(DepartmentModel).all()

        return departments
    else:
        raise HTTPException(status_code=401, detail='Could not validate')

@department_router.get('/{department_id}', response_model=DepartmentSerializer)
async def get_department(department_id: int, db: db_dependency, get_admin: dict = Depends(get_current_user)):
    current_admin = db.query(User).filter(User.id == get_admin['user_id']).first()
    department = db.query(DepartmentModel).filter(DepartmentModel.id == department_id).first()

    if not department:
        raise HTTPException(status_code=404, detail='Could not find department')
    
    if current_admin.role == UserRole.admin:
        return department
    else:
        raise HTTPException(status_code=401, detail='Could not validate')