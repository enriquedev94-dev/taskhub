
class AppException(Exception):
    """Base class for all application-specific exceptions."""
    status_code: int
    code: str
    message: str