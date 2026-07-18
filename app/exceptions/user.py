
from app.exceptions.base import AppException

class EmailAlreadyExistsError(AppException):
    """Exception raised when an email already exists."""
    http_status: int = 409
    code: str = "EMAIL_ALREADY_EXISTS"
    message: str = "The email address is already in use."
