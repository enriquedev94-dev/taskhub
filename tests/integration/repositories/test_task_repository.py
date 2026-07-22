from app.repositories.task import TaskRepository
from app.models.task import Task

def test_create_task(db_session):
    repository = TaskRepository(db_session)
    task_data = Task(
        title="New Task",
        description="A new task",
        project_id=1,
    )

    result = repository.create(task_data)
    db_session.commit()

    assert result.id is not None

    saved_task = db_session.query(Task).filter(
        Task.title == "New Task"
    ).first()

    assert saved_task is not None
    assert saved_task.description == "A new task"

def test_get_task_by_id(db_session):
    repository = TaskRepository(db_session)

    task = Task(
        title="Test Task",
        description="A test task",
        project_id=1,
    )

    db_session.add(task)
    db_session.commit()

    result = repository.get_by_id(Task, task.id)
    assert result.title == "Test Task"
    assert result.description == "A test task"

def test_get_tasks_by_project_id(db_session):
    repository = TaskRepository(db_session)

    task1 = Task(
        title="Task 1",
        description="First task",
        project_id=1,
    )
    task2 = Task(
        title="Task 2",
        description="Second task",
        project_id=1,
    )
    task3 = Task(
        title="Task 3",
        description="Third task",
        project_id=2,
    )

    db_session.add_all([task1, task2, task3])
    db_session.commit()

    result = repository.get_by_project_id(1)
    assert len(result) == 2
    assert all(task.project_id == 1 for task in result)

def test_delete_task(db_session):
    repository = TaskRepository(db_session)

    task = Task(
        title="Task to Delete",
        description="This task will be deleted",
        project_id=1,
    )

    db_session.add(task)
    db_session.commit()

    repository.delete(task)
    db_session.commit()

    deleted_task = db_session.query(Task).filter(
        Task.id == task.id
    ).first()

    assert deleted_task is None