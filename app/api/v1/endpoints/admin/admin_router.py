from fastapi import APIRouter

from app.api.v1.endpoints.admin.user_endpoint import user_router
from app.api.v1.endpoints.admin.task_endpoint import task_router
from app.api.v1.endpoints.admin.team_endpoint import team_router
from app.api.v1.endpoints.admin.department_endpoint import department_router

admin_router = APIRouter(prefix='/admin', tags=['admin'])

admin_router.include_router(user_router)
admin_router.include_router(task_router)
admin_router.include_router(team_router)
admin_router.include_router(department_router)

