from app.repositories.project import ProjectRepository
from app.models.project import Project

def test_get_by_id(db_session):
    repository = ProjectRepository(db_session)

    project = Project(
        name="Test Project",
        description="A test project",
        owner_id=1
    )

    db_session.add(project)
    db_session.commit()
    result = repository.get_by_id(Project,project.id)
    assert result.name == "Test Project"
    assert result.description == "A test project"

def test_get_projects_by_owner(db_session):
    repository = ProjectRepository(db_session)
    
    project1 = Project(
        name="Project 1",
        description="First project",
        owner_id=1
    )
    project2 = Project(
        name="Project 2",
        description="Second project",
        owner_id=1
    )
    project3 = Project(
        name="Project 3",
        description="Third project",
        owner_id=2
    )

    db_session.add_all([project1, project2, project3])
    db_session.commit()

    result = repository.get_by_owner_id(1)
    assert len(result) == 2
    assert all(project.owner_id == 1 for project in result)

def test_create_project(db_session):
    repository = ProjectRepository(db_session)
    project_data = Project(
        name="New Project",
        description="A new project",
        owner_id=1
    )
    result = repository.create(project_data)
    db_session.commit()

    assert result.id is not None

    saved_project = db_session.query(Project).filter(
        Project.name == "New Project"
    ).first()

    assert saved_project is not None

def test_update_project(db_session):
    repository = ProjectRepository(db_session)
    project = Project(
        name="Old Project",
        description="An old project",
        owner_id=1
    )

    db_session.add(project)
    db_session.commit()

    assert project.name == "Old Project"

    project.name = "updated project"
    project.description = "An updated project"
    db_session.commit()
    updated_project = db_session.query(Project).filter(
        Project.name == "updated project"
    )

    assert updated_project.first() is not None
    assert updated_project.first().description == "An updated project"

def test_delete_project(db_session):
    repository = ProjectRepository(db_session)
    project = Project(
        name="Project to Delete",
        description="This project will be deleted",
        owner_id=1
    )

    db_session.add(project)
    db_session.commit()

    assert project.id is not None

    repository.delete(project)
    db_session.commit()

    deleted_project = db_session.query(Project).filter(
        Project.id == project.id
    ).first()

    assert deleted_project is None

