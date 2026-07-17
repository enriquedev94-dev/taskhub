from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.dependencies import get_db

router = APIRouter()

@router.get("/health", tags=["Health"])
async def health(db: Session = Depends(get_db)):
    return {"status": "ok"}