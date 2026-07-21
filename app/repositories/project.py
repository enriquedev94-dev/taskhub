from app.models import Project
from app.repositories.base import BaseRepository

class ProjectRepository(BaseRepository):
    def get_by_owner_id(self, owner_id: int):
        return self.db.query(Project).filter(Project.owner_id == owner_id).all()
    