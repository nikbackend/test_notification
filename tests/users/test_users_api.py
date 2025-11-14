VALID_REG_DATA = {
    "username": "testuser",
    "password": "StrongPass123",
    "avatar_url": "https://example.com/avatar.jpg",
}

INVALID_REG_DATA = {
    "username": "",  # пустое имя
    "password": "123",  # слабый пароль
    "avatar_url": "not-a-url",
}

LOGIN_DATA = {
    "username": VALID_REG_DATA["username"],
    "password": VALID_REG_DATA["password"],
}


async def test_register_user_success(client):
    response = await client.post("/users/auth/register", json=VALID_REG_DATA)
    assert response.status_code == 201
    data = response.json()
    assert "user_id" in data
    assert "access_token" in data


async def test_register_duplicate_username(client):
    await client.post("/users/auth/register", json=VALID_REG_DATA)
    response = await client.post("/users/auth/register", json=VALID_REG_DATA)
    assert response.status_code == 400
    assert response.json()["detail"] == "Пользователь с таким именем уже существует"


async def test_register_invalid_data(client):
    response = await client.post("/users/auth/register", json=INVALID_REG_DATA)
    assert response.status_code == 422


async def test_login_success(client):
    # сначала регистрируем пользователя
    await client.post("/users/auth/register", json=VALID_REG_DATA)
    response = await client.post(
        "/users/auth/login",
        json=LOGIN_DATA,
    )
    assert response.status_code == 200
    data = response.json()
    assert "user_id" in data
    assert "access_token" in data


async def test_login_wrong_password(client):
    register_response = await client.post("/users/auth/register", json=VALID_REG_DATA)
    assert register_response.status_code == 201
    response = await client.post(
        "/users/auth/login",
        json={"username": VALID_REG_DATA["username"], "password": "wrongpass"},
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Неверный логин или пароль"


async def test_login_nonexistent_user(client):
    response = await client.post(
        "/users/auth/login",
        json={"username": "notexist", "password": "nopass"},
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Неверный логин или пароль"
