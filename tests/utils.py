from httpx import AsyncClient

from main import app


async def get_async_client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
