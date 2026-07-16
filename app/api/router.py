from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.dependencies import get_db

router = APIRouter()

@router.get("/health", tags=["Health"])
async def health(db: Session = Depends(get_db)):
    return {"status": "ok"}

@router.get("/debug/session", tags=["Debug"])
async def debug_session(db: Session = Depends(get_db)):
    return {"session_type": type(db).__name__, "is_active": db.is_active}