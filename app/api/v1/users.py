from app.api.router import router
from app.schemas.user import UserCreate
from app.services.user import UserService
from fastapi import Depends
from app.api.dependencies import get_user_service

@router.post('/users', tags=["Users"])
async def create_user(user: UserCreate, user_service: UserService = Depends(get_user_service)):
    return user_service.create_user(user)
