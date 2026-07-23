from sqlalchemy import select

from app.models import Project
from app.repositories.base import BaseRepository
from sqlalchemy.orm import selectinload

class ProjectRepository(BaseRepository):
    def get_by_owner_id(self, owner_id: int):
        return self.db.execute(
            select(Project)
            .options(selectinload(Project.tasks))
            .where(Project.owner_id == owner_id)
        ).scalars().all()
    