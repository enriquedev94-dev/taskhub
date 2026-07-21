from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.api.v1.users import router as user_router
from app.api.v1.auth import router as auth_router
from app.api.v1.projects import router as project_router

router = APIRouter()

router.include_router(user_router, prefix="/users", tags=["Users"])
router.include_router(auth_router, prefix="/auth", tags=["Auth"])
router.include_router(project_router, prefix="/projects", tags=["Projects"])

@router.get("/debug/session", tags=["Debug"])
async def debug_session(db: Session = Depends(get_db)):
    return {"session_type": type(db).__name__, "is_active": db.is_active}