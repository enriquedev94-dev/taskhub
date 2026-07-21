from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.router import router
from app.core.config import settings
from app.exceptions.base import AppException
from app.middlewares.exceptions import app_exception_handler
from app.core.logging import setup_logging

setup_logging()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting Taskhub api...")
    yield
    print("Stopping Taskhub api...")

app = FastAPI(
    title=settings.app_name,
    lifespan=lifespan,
)

app.include_router(router, prefix="/api/v1")
app.add_exception_handler(AppException, app_exception_handler)