from app.repositories.user import UserRepository
from app.schemas.user import UserCreate
from app.repositories.project import ProjectRepository
from app.models import Project
from app.models import User
from app.exceptions import EmailAlreadyExistsError

class UserService:
    def __init__(self, user_repository: UserRepository, project_repository: ProjectRepository):
        self.user_repository = user_repository
        self.project_repository = project_repository

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
                password_hash=data.password
            )

            self.user_repository.create(new_user)
            self.user_repository.db.flush()

            new_project = Project(
                name="My first project",
                description="This is your first project",
                owner_id=new_user.id
            )

            self.project_repository.create(new_project)
            self.user_repository.db.commit()
            self.user_repository.db.refresh(new_user)
            return new_user
        except Exception as e:
            self.user_repository.db.rollback()
            raise

