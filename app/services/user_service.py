from app.repositories.user import UserRepository
from app.schemas.user import UserCreate
from app.repositories.project import ProjectRepository
from app.models import Project
from app.models import User
from app.exceptions import EmailAlreadyExistsError, InvalidCredentialsError
from app.services.password import PasswordService
from app.services.token import TokenService
from app.core.logging import get_logger

logger = get_logger(__name__)
class UserService:
    def __init__(self, user_repository: UserRepository, project_repository: ProjectRepository, password_service: PasswordService, token_service: TokenService):
        self.user_repository = user_repository
        self.project_repository = project_repository
        self.password_service = password_service
        self.token_service = token_service

    def create_user(self, data: UserCreate):
        try:
            existing_user = self.user_repository.get_by_email(data.email)
            if existing_user:
                raise EmailAlreadyExistsError(
                    details={"field": "email"}
                )
            new_user = User(
                email=data.email,
                name=data.name,
                password_hash=self.password_service.hash(data.password)
            )

            self.user_repository.create(new_user)
            self.user_repository.db.flush()

            new_project = Project(
                name="My first project",
                description="This is your first project",
                owner_id=new_user.id
            )
            logger.info(f"Creating default project for user {new_user.id}")

            self.project_repository.create(new_project)
            self.user_repository.db.commit()
            self.user_repository.db.refresh(new_user)
            logger.info(f"User {new_user.id} created successfully with default project {new_project.id}")
            return new_user
        except Exception as e:
            self.user_repository.db.rollback()
            logger.error(f"Error creating user: {e}")
            raise

    def login(self, email: str, password: str):
        user = self.user_repository.get_by_email(email)
        if not user or not self.password_service.verify(password, user.password_hash):
            raise InvalidCredentialsError(
                details={"reason": "invalid_credentials"}
            )
        token = self.token_service.create_access_token(user.id)
        logger.info(f"User {user.id} logged in successfully")
        return {
            "access_token": token,
            "token_type": "bearer"
        }
        
