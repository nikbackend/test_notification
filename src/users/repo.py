from tortoise.backends.base.client import BaseDBAsyncClient

from src.core.security import hash_password
from src.users.model import User


class UserRepo:
    async def create_user(
        self, username: str, avatar_url: str, password: str, conn: BaseDBAsyncClient
    ):
        hashed = hash_password(password)
        user = await User.create(
            username=username, avatar_url=avatar_url, password=hashed, using_db=conn
        )
        return user

    async def get_user_by_username(self, username: str, conn: BaseDBAsyncClient):
        return await User.get_or_none(username=username, using_db=conn)
