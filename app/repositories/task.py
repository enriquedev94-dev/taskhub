from app.models import Task
from app.repositories.base import BaseRepository

class TaskRepository(BaseRepository):

    def _build_project_query(
        self,
        project_id: int,
        search: str | None = None,
    ):
        query = self.db.query(Task).filter(
            Task.project_id == project_id
        )

        if search:
            query = query.filter(
                Task.title.ilike(f"%{search}%")
            )
        return query
    
    def get_by_project_id(self, project_id: int, limit: int, offset: int, search: str | None = None):
        return self._build_project_query(project_id, search=search).limit(limit).offset(offset).all()
    
    def count_by_project_id(self, project_id: int, search: str | None = None):
        return self._build_project_query(project_id, search=search).count()