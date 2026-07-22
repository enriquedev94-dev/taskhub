import pytest

@pytest.mark.asyncio
async def test_create_task(client, auth_headers, test_project):
    response = await client.post(
        f'/api/v1/projects/{test_project.id}/tasks',
        json={
            "title": "Test Task",
            "description": "This is a test task"
        },
        headers=auth_headers
    )

    assert response.status_code == 200
    data = response.json()

    assert data["title"] == "Test Task"
    assert data["description"] == "This is a test task"
    assert data["project_id"] == test_project.id