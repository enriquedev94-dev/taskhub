import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from httpx import AsyncClient, ASGITransport
from app.db.dependencies import get_db
import pytest_asyncio
from app.db.base import Base
from app.models import User, Project, Task
from app.main import app
from app.services.password import PasswordService

engine = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


@pytest.fixture()
def db_session():
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

@pytest_asyncio.fixture()
async def client(db_session):
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as Client:
        yield Client

    app.dependency_overrides.clear()

@pytest_asyncio.fixture()
def test_user(db_session):
    password_service = PasswordService()

    user = User(
        name="Test User",
        email="test@example.com",
        password_hash=password_service.hash("password123")
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user

@pytest_asyncio.fixture()
async def auth_headers(client, test_user):
    response = await client.post(
        '/api/v1/auth/login',
        json={
            "email": test_user.email,
            "password": "password123"
        }
    )
    token = response.json()["access_token"]
    return {
        "Authorization": f"Bearer {token}"
    }

@pytest.fixture()
def test_project(db_session, test_user):
    project = Project(
        name="Test Project",
        description="This is a test project",
        owner_id=test_user.id
    )
    db_session.add(project)
    db_session.commit()
    db_session.refresh(project)
    return project