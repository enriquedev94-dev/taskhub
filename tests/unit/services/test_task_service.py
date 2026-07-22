import pytest
from app.services.task_service import TaskService
from app.repositories.task import TaskRepository
from app.repositories.project import ProjectRepository
from app.models.user import User
from app.schemas.task import TaskCreate
from app.exceptions.project import ProjectNotFoundError
from app.models.project import Project

def test_create_task_successfully(mocker):
    mock_task_repository = mocker.Mock(TaskRepository)
    mock_task_repository.db = mocker.Mock()
    mock_project_repository = mocker.Mock(ProjectRepository)
    mock_project_repository.get_by_id.return_value = Project(id=1, name="Test Project", owner_id=1)  # Simulate project not found
    task_service = TaskService(
        task_repository=mock_task_repository,
        project_repository=mock_project_repository
    )

    current_user = User(id=1, name="Test User", email="testuser@gmail.com", password_hash="hashed_password")
    task_data = TaskCreate(
        title="New Task", description="This is a new task"
    )
    task_service.create_task(task_data, project_id=1, current_user=current_user)
    mock_task_repository.create.assert_called_once()
    mock_project_repository.get_by_id.assert_called_once_with(Project, 1)
    created_task = mock_task_repository.create.call_args.args[0]
    assert created_task.title == "New Task"
    assert created_task.description == "This is a new task"
    assert created_task.project_id == 1

def test_create_task_project_not_found(mocker):
    mock_task_repository = mocker.Mock(TaskRepository)
    mock_project_repository = mocker.Mock(ProjectRepository)
    mock_project_repository.get_by_id.return_value = None  # Simulate project not found
    task_service = TaskService(
        task_repository=mock_task_repository,
        project_repository=mock_project_repository
    )

    current_user = User(id=1, name="Test User", email="testuser@gmail.com", password_hash="hashed_password")
    task_data = TaskCreate(
        title="New Task", description="This is a new task"
    )
    with pytest.raises(ProjectNotFoundError):
        task_service.create_task(task_data, project_id=1, current_user=current_user)
    