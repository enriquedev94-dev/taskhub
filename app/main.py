from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.router import router
from app.core.config import settings

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