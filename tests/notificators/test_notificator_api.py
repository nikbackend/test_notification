import pytest
from httpx import AsyncClient

from src.notificator.enum import EnumShema

VALID_USER = {
    "username": "testuser",
    "password": "StrongPass123",
    "avatar_url": "https://example.com/avatar.jpg",
}

VALID_NOTIFICATION = {"type": EnumShema.LIKE, "text": "This is a test notification"}


@pytest.fixture
async def auth_headers(client: AsyncClient):
    response = await client.post("/users/auth/register", json=VALID_USER)
    assert response.status_code == 201

    token = response.json()["access_token"]
    return {"access-token": f"{token}"}


@pytest.mark.asyncio
async def test_create_notification(client: AsyncClient, auth_headers):
    print(f"{auth_headers}")
    response = await client.post("/notifications/", json=VALID_NOTIFICATION, headers=auth_headers)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert "user_id" in data
    assert "created_at" in data


@pytest.mark.asyncio
async def test_list_notifications(client: AsyncClient, auth_headers):
    notification_response = await client.post(
        "/notifications/", json=VALID_NOTIFICATION, headers=auth_headers
    )
    assert notification_response.status_code == 201
    response = await client.get("/notifications/", headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


@pytest.mark.asyncio
async def test_delete_notification(client: AsyncClient, auth_headers):
    response_create = await client.post(
        "/notifications/", json=VALID_NOTIFICATION, headers=auth_headers
    )
    notif_id = response_create.json()["id"]
    response_delete = await client.delete(f"/notifications/{notif_id}", headers=auth_headers)
    assert response_delete.status_code == 200


@pytest.mark.asyncio
async def test_delete_notification_forbidden(client: AsyncClient, auth_headers):
    await client.post(
        "/users/auth/register",
        json={
            "username": "otheruser",
            "password": "StrongPass123",
            "avatar_url": "https://example.com/avatar.jpg",
        },
    )
    other_token_resp = await client.post(
        "/users/auth/login", json={"username": "otheruser", "password": "StrongPass123"}
    )
    assert other_token_resp.status_code == 200

    response_create = await client.post(
        "/notifications/",
        json=VALID_NOTIFICATION,
        headers={"access-token": f"{other_token_resp.json()['access_token']}"},
    )
    assert response_create.status_code == 201

    notification_id = response_create.json()["id"]
    response_delete = await client.delete(f"/notifications/{notification_id}", headers=auth_headers)
    assert response_delete.status_code == 404
