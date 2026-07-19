from fastapi import Request
from fastapi.responses import JSONResponse
from app.exceptions.base import AppException

async def app_exception_handler(
        request: Request,
        exc: AppException
):
    return JSONResponse(
        status_code=exc.http_status,
        content={
            "code": exc.code,
            "message": exc.message,
            "details": exc.details
        }
    )