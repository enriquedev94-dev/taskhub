from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(nullable=True)
    status: Mapped[str] = mapped_column(
        String(50),
        default="todo",
    )
    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id")
    )
    project: Mapped["Project"] = relationship()