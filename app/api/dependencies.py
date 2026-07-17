from app.repositories.user import UserRepository
from app.services.user import UserService
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_db

def get_user_service(db: Session = Depends(get_db)) -> UserService:
    repository = UserRepository(db)
    return UserService(repository)