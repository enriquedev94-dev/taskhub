from app.repositories.user import UserRepository
from app.schemas.user import UserCreate
class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, data: UserCreate):
        return { "message": "User created successfully"}



