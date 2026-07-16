from collections.abc import Generator
from sqlalchemy.orm import Session
from app.db.database import SessionLocal

def get_db() -> Generator[Session, None, None]:
    print("Getting database session...")
    db = SessionLocal()

    try:
        yield db
    finally:
        print("Closing database session...")
        db.close()