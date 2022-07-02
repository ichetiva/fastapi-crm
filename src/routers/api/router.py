from fastapi import APIRouter

from .users.router import router as users_router
from .auth.router import router as auth_router

router = APIRouter(
    prefix='/api'
)
router.include_router(users_router)
router.include_router(auth_router)
