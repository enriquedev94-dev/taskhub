from app.models import Task
from app.repositories.base import BaseRepository

class TaskRepository(BaseRepository):
    def get_by_project_id(self, project_id: int):
        return self.db.query(Task).filter(Task.project_id == project_id).all()