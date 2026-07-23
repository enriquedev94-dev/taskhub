from app.models import Task
from app.repositories.base import BaseRepository

class TaskRepository(BaseRepository):
    def get_by_project_id(self, project_id: int, limit: int, offset: int):
        return self.db.query(Task).filter(Task.project_id == project_id).limit(limit).offset(offset).all()
    
    def count_by_project_id(self, project_id: int):
        return self.db.query(Task).filter(Task.project_id == project_id).count()