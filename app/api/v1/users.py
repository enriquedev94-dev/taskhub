from app.schemas.user import UserCreate
from app.schemas.auth import AuthRequest
from app.services.user_service import UserService
from fastapi import APIRouter, Depends
from typing import Annotated
from app.api.dependencies import get_current_user, get_user_service
from app.models import User

router = APIRouter()

@router.post('/users', tags=["Users"])
async def create_user(user: UserCreate, user_service: Annotated[UserService, Depends(get_user_service)]):
    return user_service.create_user(user)

@router.get('/users/me', tags=["Users"])
async def get_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user

