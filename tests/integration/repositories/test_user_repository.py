from app.repositories.user import UserRepository
from app.models.user import User

def test_get_by_email_returns_user(db_session):
    repository = UserRepository(db_session)

    user = User(
        email="testuser@gmail.com",
        name="Test User",
        password_hash="hashed_password"
    )

    db_session.add(user)
    db_session.commit()
    result = repository.get_by_email("testuser@gmail.com")
    assert result.email == "testuser@gmail.com"

def test_get_by_email_returns_none_for_nonexistent_user(db_session):
    repository = UserRepository(db_session)
    result = repository.get_by_email("hola@test.com")
    assert result is None

def test_create_user(db_session):
    repository = UserRepository(db_session)
    user_data = User(
        name="New User",
        email="newuser@gmail.com",
        password_hash="new_hashed_password"
    )
    result = repository.create(user_data)
    db_session.commit()

    assert result.id is not None

    saved_user = db_session.query(User).filter(
        User.email == "newuser@gmail.com"
    ).first()

    assert saved_user is not None
    assert saved_user.name == "New User"