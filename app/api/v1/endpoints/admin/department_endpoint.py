from fastapi import APIRouter, Depends

from starlette import status

from app.core.database import db_dependency
from app.core.security import get_current_user
from app.models.user import User
from app.schema.department import Department
from app.services.admin.department.create_service import create_service

department_router = APIRouter(prefix='/departments')

@department_router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_department(create_department: Department, db: db_dependency, get_admin: dict = Depends(get_current_user)):
    current_admin = db.query(User).filter(User.id == get_admin['user_id']).first()
    department = create_service(current_admin, create_department, db)

    return department