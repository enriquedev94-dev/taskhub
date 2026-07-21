from app.exceptions.base import AppException

class ProjectNotFoundError(AppException):
    """Exception raised when a project is not found."""
    http_status: int = 404
    code: str = "PROJECT_NOT_FOUND"
    message: str = "The requested project was not found."

class ProjectForbiddenError(AppException):
    """Exception raised when a user tries to access a project they do not own."""
    http_status: int = 403
    code: str = "PROJECT_FORBIDDEN"
    message: str = "You do not have permission to access this project."