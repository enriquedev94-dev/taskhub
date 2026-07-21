from app.exceptions.project import ProjectNotFoundError, ProjectForbiddenError
from app.repositories.project import ProjectRepository
from app.schemas.project import ProjectCreate
from app.models import Project
from app.models import User

class ProjectService:
    def __init__(self, project_repository: ProjectRepository):
        self.project_repository = project_repository

    def create_project(self, data: ProjectCreate, current_user: User):
        new_project = Project(
            name=data.name,
            description=data.description,
            owner_id=current_user.id
        )
        self.project_repository.create(new_project)
        self.project_repository.db.commit()
        self.project_repository.db.refresh(new_project)
        return new_project
    
    def get_projects(self, owner_id: int):
        return self.project_repository.get_by_owner_id(owner_id)
    
    def get_project(self, project_id: int, owner_id: int):
        project = self.project_repository.get_by_id(Project, project_id)
        if project is None or project.owner_id != owner_id:
            raise ProjectNotFoundError(
                details={"project_id": project_id}
            )
        return project
    
    def update_project(self, project_id: int, data: ProjectCreate, current_user: User):
        project = self.project_repository.get_by_id(Project, project_id)
        if project is None or project.owner_id != current_user.id:
            raise ProjectNotFoundError(
                details={"project_id": project_id}
            )
        project.name = data.name
        project.description = data.description
        self.project_repository.db.commit()
        self.project_repository.db.refresh(project)
        return project
    
    def delete_project(self, project_id: int, current_user: User):
        project = self.project_repository.get_by_id(Project, project_id)
        if project is None or project.owner_id != current_user.id:
            raise ProjectNotFoundError(
                details={"project_id": project_id}
            )
        self.project_repository.delete(project)
        self.project_repository.db.commit()
        return