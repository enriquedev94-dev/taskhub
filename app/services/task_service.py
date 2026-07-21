from app.repositories.task import TaskRepository
from app.models import Task, Project, User
from app.exceptions.project import ProjectNotFoundError
from app.exceptions import TaskNotFoundError
from app.repositories.project import ProjectRepository
from app.schemas.task import TaskCreate
from app.core.logging import get_logger
logger = get_logger(__name__)
class TaskService:
    def __init__(self, task_repository: TaskRepository, project_repository: ProjectRepository):
        self.task_repository = task_repository
        self.project_repository = project_repository

    def create_task(self, data: TaskCreate, project_id: int, current_user: User):
        project = self.project_repository.get_by_id(Project, project_id)
        if not project or project.owner_id != current_user.id:
            raise ProjectNotFoundError(
                details={"project_id": project_id},
            )
        new_task = Task(
            title=data.title,
            description=data.description,
            project_id=project_id,
        )
        logger.info(f"Creating task '{new_task.title}' for project {project_id} by user {current_user.id}")
        self.task_repository.create(new_task)
        self.task_repository.db.commit()
        self.task_repository.db.refresh(new_task)
        logger.info(f"Task '{new_task.title}' created successfully with ID {new_task.id} for project {project_id} by user {current_user.id}")
        return new_task
    
    def get_tasks(self, project_id: int, owner_id: int):
        project = self.project_repository.get_by_id(Project, project_id)
        if not project or project.owner_id != owner_id:
            raise ProjectNotFoundError(
                details={"project_id": project_id},
            )
        return self.task_repository.get_by_project_id(project_id)
    
    def get_task(self, task_id: int, owner_id: int):
        task = self.task_repository.get_by_id(Task, task_id)
        if not task or task.project.owner_id != owner_id:
            raise TaskNotFoundError(
                details={"task_id": task_id},
            )
        return task
    
    def update_task(self, task_id: int, data: TaskCreate, owner_id: int):
        task = self.task_repository.get_by_id(Task, task_id)
        if not task or task.project.owner_id != owner_id:
            raise TaskNotFoundError(
                details={"task_id": task_id},
            )
        logger.info(f"Updating task '{task.title}' (ID: {task.id}) for project {task.project_id} by user {owner_id}")
        task.title = data.title
        task.description = data.description
        task.status = data.status
        self.task_repository.db.commit()
        self.task_repository.db.refresh(task)
        logger.info(f"Task '{task.title}' (ID: {task.id}) updated successfully for project {task.project_id} by user {owner_id}")
        return task

    def delete_task(self, task_id: int, owner_id: int):
        task = self.task_repository.get_by_id(Task, task_id)
        if not task or task.project.owner_id != owner_id:
            raise TaskNotFoundError(
                details={"task_id": task_id},
            )
        self.task_repository.delete(task)
        self.task_repository.db.commit()
        logger.info(f"Task '{task.title}' (ID: {task.id}) deleted successfully for project {task.project_id} by user {owner_id}")
        return {"message": "Task deleted successfully."}