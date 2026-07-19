from app.schemas.user import UserCreate
from app.services.user_service import UserService
from fastapi import APIRouter, Depends
from typing import Annotated
from app.api.dependencies import get_user_service

router = APIRouter()

@router.post('/users', tags=["Users"])
async def create_user(user: UserCreate, user_service: Annotated[UserService, Depends(get_user_service)]):
    return user_service.create_user(user)

@router.get('/users', tags=["Users"])
async def get_user(user_service: Annotated[UserService, Depends(get_user_service)]):
    return { "message": "ok"}