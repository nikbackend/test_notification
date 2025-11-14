import pytest
from httpx import ASGITransport, AsyncClient
from tortoise import Tortoise

from main import app
from src.core.settings import TEST_TORTOISE_ORM


@pytest.fixture(scope="function")
async def client():
    # Инициализация тестовой БД
    await Tortoise.init(config=TEST_TORTOISE_ORM)
    await Tortoise.generate_schemas()

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as ac:
        yield ac

    # Очистка таблиц
    for app_models in Tortoise.apps.values():
        for model in app_models.values():
            await model.all().delete()
    await Tortoise.close_connections()
