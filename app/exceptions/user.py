
from app.exceptions.base import AppException

class UserException(AppException):
    """Base class for all user-related exceptions."""
    
    def EmailAlreadyExistsError(self, email):
