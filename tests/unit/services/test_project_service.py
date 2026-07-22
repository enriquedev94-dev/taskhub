import pytest
from app.services.project_service import ProjectService
from app.repositories.project import ProjectRepository
from app.models.user import User
from app.schemas.project import ProjectCreate
from app.models.project import Project
from app.exceptions.project import ProjectNotFoundError

def test_create_project_when_user_exists(mocker):
    mock_project_repository = mocker.Mock(ProjectRepository)
    mock_project_repository.db = mocker.Mock()
    current_user = User(
        id=1, name="Test User", email="testuser@gmail.com", password_hash="hashed_password"
    )
    project_service = ProjectService(
        project_repository=mock_project_repository
    )
    project_data = ProjectCreate(
        name="New Project", description="This is a new project"
    )
    project_service.create_project(project_data, current_user)
    mock_project_repository.create.assert_called_once()
    created_project = mock_project_repository.create.call_args.args[0]
    assert created_project.name == "New Project"
    assert created_project.description == "This is a new project"
    assert created_project.owner_id == current_user.id

def test_get_projects_by_owner_id(mocker):
    mock_project_repository = mocker.Mock(ProjectRepository)
    projects = [
        Project(
            id=1, name="Project 1", description="Description 1", owner_id=1
        ),
        Project(
            id=2, name="Project 2", description="Description 2", owner_id=1
        )
    ]
    mock_project_repository.get_by_owner_id.return_value = projects
    project_service = ProjectService(
        project_repository=mock_project_repository
    )
    result = project_service.get_projects(owner_id=1)
    assert result == projects

def test_get_project_by_id_and_owner_id(mocker):
    mock_project_repository = mocker.Mock(ProjectRepository)
    project = Project(
        id=1, name="Project 1", description="Description 1", owner_id=1
    )
    mock_project_repository.get_by_id.return_value = project
    project_service = ProjectService(
        project_repository=mock_project_repository
    )
    with pytest.raises(ProjectNotFoundError):
        project_service.get_project(project_id=1, owner_id=2)
    result = project_service.get_project(project_id=1, owner_id=1)
    assert result == project