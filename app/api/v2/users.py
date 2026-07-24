
router = APIRouter()
from fastapi import APIRouter
from app.schemas.v2.user import UserResponseV2
from typing import Annotated
from fastapi import Depends
from app.models.user import User
from app.api.dependencies import get_current_user

@router.get('/{user_id}', response_model=UserResponseV2)
async def get_me(
    current_user: Annotated[User, Depends(get_current_user)]
):
    first_name, _, last_name = current_user.name.partition(' ')
    return UserResponseV2(
        id=current_user.id,
        first_name=first_name,
        last_name=last_name,
        email=current_user.email
    )