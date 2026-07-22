from app.services.user_service import UserService
import pytest
from app.schemas.user import UserCreate
from app.repositories.user import UserRepository
from app.models.user import User
from app.exceptions.user import EmailAlreadyExistsError
 
def test_create_user_when_email_exists(mocker):
    mock_user_repository = mocker.Mock()
    mock_user_repository.get_by_email.return_value = User(
        name="Existing User", email="carlos@gmail.com"
    )
    mock_project_repository = mocker.Mock()
    mock_project_repository.db = mocker.Mock()
    mock_password_service = mocker.Mock()
    mock_token_service = mocker.Mock()
    user_service = UserService(
        user_repository=mock_user_repository,
        project_repository=mock_project_repository,
        password_service=mock_password_service,
        token_service=mock_token_service,
    )
    with pytest.raises(EmailAlreadyExistsError):
        user_service.create_user(UserCreate(name="New User", email="carlos@gmail.com", password="hashed_password"))

def test_create_user_when_email_does_not_exist(mocker):
    mock_user_repository = mocker.Mock(UserRepository)
    mock_user_repository.db = mocker.Mock()
    mock_user_repository.get_by_email.return_value = None
    mock_user_repository.create.side_effect = lambda user: setattr(user, "id", 1) or user

    mock_project_repository = mocker.Mock()
    mock_password_service = mocker.Mock()
    mock_password_service.hash.return_value = "hashed_password"
    mock_token_service = mocker.Mock()
    user_service = UserService(
        user_repository=mock_user_repository,
        project_repository=mock_project_repository,
        password_service=mock_password_service,
        token_service=mock_token_service,
    )
    user_data = UserCreate(
        name="New User", email="newuser@gmail.com", password="my_secure_password"
    )
    user_service.create_user(user_data)
    mock_user_repository.create.assert_called_once()
    mock_password_service.hash.assert_called_once_with("my_secure_password")

    created_user = mock_user_repository.create.call_args.args[0]
    assert created_user.name == "New User"
    assert created_user.email == "newuser@gmail.com"

    created_project = mock_project_repository.create.call_args.args[0]
    assert created_project.name == "My first project"
    assert created_project.description == "This is your first project"
    assert created_project.owner_id == created_user.id

    mock_project_repository.create.assert_called_once()
