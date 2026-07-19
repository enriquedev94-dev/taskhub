from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.router import router
from app.core.config import settings
from app.exceptions.base import AppException
from app.middlewares.exceptions import app_exception_handler

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting Taskhub api...")
    yield
    print("Stopping Taskhub api...")

app = FastAPI(
    title=settings.app_name,
    lifespan=lifespan,
)

app.include_router(router)
app.add_exception_handler(AppException, app_exception_handler)