from fastapi import APIRouter

from app.api.v1.endpoints.user_endpoint import user_router

router = APIRouter(prefix='/api/v1')

router.include_router(user_router)