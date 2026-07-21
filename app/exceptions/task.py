from app.exceptions.base import AppException

class TaskNotFoundError(AppException):
    """Exception raised when a task is not found."""
    http_status: int = 404
    code: str = "TASK_NOT_FOUND"
    message: str = "The requested task was not found."

class TaskForbiddenError(AppException):
    """Exception raised when a user tries to access a task they do not own."""
    http_status: int = 403
    code: str = "TASK_FORBIDDEN"
    message: str = "You do not have permission to access this task."