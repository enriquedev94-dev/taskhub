from app.repositories.user import UserRepository
from app.models.user import User
from app.exceptions import InvalidCredentialsError
from jwt.exceptions import PyJWTError
from app.services.user_service import UserService
from app.services.password import PasswordService
from app.services.token import TokenService
from app.repositories.project import ProjectRepository
from fastapi import Depends
from typing import Annotated
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.core.security import oauth2_scheme
from app.core.config import settings

def get_user_service(db: Session = Depends(get_db)) -> UserService:
    user_repository = UserRepository(db)
    project_repository = ProjectRepository(db)
    password_service = PasswordService()
    token_service = TokenService(secret_key=settings.secret_key)

    return UserService(
        user_repository=user_repository,
        project_repository=project_repository,
        password_service=password_service,
        token_service=token_service
    )

def get_token_service() -> TokenService:
    return TokenService(secret_key=settings.secret_key)

def get_current_user(
    db: Annotated[Session, Depends(get_db)],
    token: Annotated[str, Depends(oauth2_scheme)],
    token_service: Annotated[TokenService, Depends(get_token_service)]
):
    try:
        payload = token_service.verify_access_token(token)
        print(f"Decoded payload from token: {payload}")  # Debugging line
        user_id = payload.get("sub")
        print(f"Decoded user_id from token: {user_id}")  # Debugging line
        if not user_id:
            raise InvalidCredentialsError(
                details={"error": "Invalid credentials"}
            )
            
        user = UserRepository(db).get_by_id(User, int(user_id))
        if not user:
            raise InvalidCredentialsError(
                details={"error": "Invalid credentials"}
            )
        return user
    except InvalidCredentialsError:
        raise
    except PyJWTError as e:
        raise InvalidCredentialsError(
            details={"error": "Invalid credentials"}
        ) from e