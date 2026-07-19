from app.models import User
from app.repositories.base import BaseRepository

class UserRepository(BaseRepository):
    def get_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()
        
