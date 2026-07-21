from fastapi import APIRouter
from fastapi import Depends
from typing import Annotated
from app.schemas.task import TaskCreate
from app.services.task_service import TaskService
from app.api.dependencies import get_current_user, get_task_service
from app.models import User
router = APIRouter()

@router.get("/{task_id}")
async def get_task(task_id: int, task_service: Annotated[TaskService, Depends(get_task_service)], current_user: Annotated[User, Depends(get_current_user)]):
    return task_service.get_task(task_id=task_id, owner_id=current_user.id)

@router.patch('/{task_id}')
async def update_task(task_id: int, task_data: TaskCreate, task_service: Annotated[TaskService, Depends(get_task_service)], current_user: Annotated[User, Depends(get_current_user)]):
    return task_service.update_task(task_id=task_id, data=task_data, owner_id=current_user.id)

@router.delete('/{task_id}')
async def delete_task(task_id: int, task_service: Annotated[TaskService, Depends(get_task_service)], current_user: Annotated[User, Depends(get_current_user)]):
    return task_service.delete_task(task_id=task_id, owner_id=current_user.id)