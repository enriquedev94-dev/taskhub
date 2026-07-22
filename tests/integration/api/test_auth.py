import pytest


@pytest.mark.asyncio
async def test_login_success(client, test_user):
    response = await client.post(
        '/api/v1/auth/login',
        json={
            "email": test_user.email,
            "password": 'password123'
        }
    )
    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"

@pytest.mark.asyncio
async def test_login_failure(client, test_user):
    response = await client.post(
        '/api/v1/auth/login',
        json={
            "email": test_user.email,
            "password": 'wrongpassword'
        }
    )
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_login_with_non_existing_user(client):
    response = await client.post(
        '/api/v1/auth/login',
        json={
            "email": 'nonexisting@example.com',
            "password": 'password123'
        }
    )
    assert response.status_code == 401