from fastapi import APIRouter

from app.api.v1.endpoints.admin.admin_user_endpoint import admin_user_router

admin_router = APIRouter(prefix='/admin', tags=['admin'])

admin_router.include_router(admin_user_router)

