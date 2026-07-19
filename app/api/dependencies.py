from app.repositories.user import UserRepository
from app.services.user_service import UserService
from app.repositories.project import ProjectRepository
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.dependencies import get_db

def get_user_service(db: Session = Depends(get_db)) -> UserService:
    repository = UserRepository(db)
    return UserService(user_repository=repository, project_repository=ProjectRepository(db))