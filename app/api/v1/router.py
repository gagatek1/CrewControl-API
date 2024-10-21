from fastapi import APIRouter

from app.api.v1.endpoints.user_endpoint import user_router
from app.api.v1.endpoints.admin.admin_router import admin_router
from app.api.v1.endpoints.task_endpoint import task_router
from app.api.v1.endpoints.team_endpoint import team_router

router = APIRouter(prefix='/api/v1')

router.include_router(user_router)
router.include_router(admin_router)
router.include_router(task_router)
router.include_router(team_router)