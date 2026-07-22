from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Index
from sqlalchemy import Enum
from app.schemas.task import TaskStatus
from app.db.base import Base

class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(nullable=True)
    status: Mapped[TaskStatus] = mapped_column(
        Enum(TaskStatus),
        default=TaskStatus.TODO,
    )
    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id")
    )
    project: Mapped["Project"] = relationship(
        back_populates="tasks"
    )
    __table_args__ = (
        Index("ix_tasks_project_id", "project_id"),
    )