from fastapi import APIRouter

from app.api.v1.endpoints.user_endpoint import user_router
from app.api.v1.endpoints.admin_endpoint import admin_router

router = APIRouter(prefix='/api/v1')

router.include_router(user_router)
router.include_router(admin_router)