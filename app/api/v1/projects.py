
from fastapi import APIRouter, Depends
from typing import Annotated
from app.schemas.project import ProjectCreate
from app.services.project_service import ProjectService
from app.models import User
from app.api.dependencies import get_current_user, get_project_service

router = APIRouter()

@router.post('/')
async def create_project(project: ProjectCreate, project_service: Annotated[ProjectService, Depends(get_project_service)], current_user: Annotated[User, Depends(get_current_user)]):
    return project_service.create_project(data=project, current_user=current_user)

@router.get('/')
async def get_projects(project_service: Annotated[ProjectService, Depends(get_project_service)], current_user: Annotated[User, Depends(get_current_user)]):
    return project_service.get_projects(owner_id=current_user.id)

@router.get('/{project_id}')
async def get_project(project_id: int, project_service: Annotated[ProjectService, Depends(get_project_service)], current_user: Annotated[User, Depends(get_current_user)]):
    return project_service.get_project(project_id=project_id, owner_id=current_user.id)

@router.patch('/{project_id}')
async def update_project(project_id: int, project: ProjectCreate, project_service: Annotated[ProjectService, Depends(get_project_service)], current_user: Annotated[User, Depends(get_current_user)]):
    return project_service.update_project(project_id=project_id, data=project, current_user=current_user)

@router.delete('/{project_id}')
async def delete_project(project_id: int, project_service: Annotated[ProjectService, Depends(get_project_service)], current_user: Annotated[User, Depends(get_current_user)]):
    return project_service.delete_project(project_id=project_id, current_user=current_user)