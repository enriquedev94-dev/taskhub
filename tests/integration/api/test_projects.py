import pytest

@pytest.mark.asyncio
async def test_create_project(client, auth_headers):
    response = await client.post(
        '/api/v1/projects/',
        json={
            "name": "Test Project",
            "description": "This is a test project"
        },
        headers=auth_headers
    )

    assert response.status_code == 200
    data = response.json()

    assert data["name"] == "Test Project"
    assert data["description"] == "This is a test project"

@pytest.mark.asyncio
async def test_get_projects_by_owner_id(client, auth_headers):
    await client.post(
        '/api/v1/projects/',
        json={
            "name": "Test Project",
            "description": "This is a test project"
        },
        headers=auth_headers
    )

    response = await client.get(
        '/api/v1/projects/',
        headers=auth_headers
    )

    assert response.status_code == 200
    data = response.json()

    assert len(data) == 1
    assert data[0]["name"] == "Test Project"
    
    