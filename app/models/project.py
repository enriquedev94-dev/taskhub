from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(nullable=True)
    owner_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )
    owner: Mapped["User"] = relationship()
    tasks: Mapped[list["Task"]] = relationship(
        back_populates="project"
        )