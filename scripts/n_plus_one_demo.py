from app.db.database import SessionLocal
from app.models import Project
from sqlalchemy.orm import selectinload

db = SessionLocal()


projects = (
    db.query(Project)
    .options(selectinload(Project.tasks))
    .limit(5)
    .all()
)
print(f"Projects loaded: {len(projects)}")

for project in projects:
    print(project.name)
    print(len(project.tasks))