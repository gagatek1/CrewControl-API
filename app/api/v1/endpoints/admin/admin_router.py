from fastapi import APIRouter

from app.api.v1.endpoints.admin.user_endpoint import user_router
from app.api.v1.endpoints.admin.task_endpoint import task_router

admin_router = APIRouter(prefix='/admin', tags=['admin'])

admin_router.include_router(user_router)
admin_router.include_router(task_router)

