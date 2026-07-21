from app.services.user_service import UserService
from app.schemas.auth import AuthRequest
from fastapi import APIRouter, Depends
from typing import Annotated
from app.api.dependencies import get_user_service
router = APIRouter()

@router.post('/login')
async def login(data: AuthRequest, user_service: Annotated[UserService, Depends(get_user_service)]):
    return user_service.login(data.email, data.password)

