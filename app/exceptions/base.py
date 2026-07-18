
class AppException(Exception):
    """Base class for all application-specific exceptions."""
    http_status: int = 500
    code: str = "UNKNOWN_ERROR"
    message: str = "An unknown error occurred."
    details: dict | None = None

    def __init__(self, details: dict | None = None):
        self.details = details
        super().__init__(self.message)