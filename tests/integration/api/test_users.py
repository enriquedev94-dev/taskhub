import pytest

@pytest.mark.asyncio
async def test_create_user_success(client):
    response = await client.post(
        '/api/v1/users/',
        json={
            "name": "New User",
            "email": "newtest@example.com",
            "password": "password123"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "New User"
    assert data["email"] == "newtest@example.com"
    assert "password" not in data
    assert "password_hash" not in data

@pytest.mark.asyncio
async def test_create_user_duplicate_email(client, test_user):
    response = await client.post(
        '/api/v1/users/',
        json={
            "name": "Duplicate User",
            "email": test_user.email,
            "password": "password123"
        }
    )

    assert response.status_code == 409
    data = response.json()
    assert "details" in data