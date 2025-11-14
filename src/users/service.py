from typing import Annotated

from fastapi import Depends
from tortoise.backends.base.client import BaseDBAsyncClient

from src.core.exceptions import (
    ExistsException,
    NoCreateException,
    UnauthorizedException,
)
from src.core.security import create_auth_token, verify_password
from src.users.repo import UserRepo
from src.users.schemes import LoginResponseSchema, RegistrationSchema


class UserService:
    def __init__(self):
        self.repo = UserRepo()

    async def create_user(self, data: RegistrationSchema, db: BaseDBAsyncClient):
        existing_user = await self.repo.get_user_by_username(data.username, conn=db)
        if existing_user:
            raise ExistsException(detail="Пользователь с таким именем уже существует")

        try:
            user = await self.repo.create_user(**data.model_dump(), conn=db)
        except Exception as exc:
            raise NoCreateException(f"Ошибка при создании пользователя: {str(exc)}")

        access_token = create_auth_token(str(user.id), "access")
        refresh_token = create_auth_token(str(user.id), "refresh")
        return LoginResponseSchema(
            user_id=user.id,
            access_token=access_token,
            refresh_token=refresh_token,
            token_type="bearer",
        )

    async def login_user(self, username: str, password: str, db: BaseDBAsyncClient):
        user = await self.repo.get_user_by_username(username, conn=db)
        if not user or not verify_password(password, user.password):
            raise UnauthorizedException("Неверный логин или пароль")

        access_token = create_auth_token(str(user.id), "access")
        refresh_token = create_auth_token(str(user.id), "refresh")
        return LoginResponseSchema(
            user_id=user.id,
            access_token=access_token,
            refresh_token=refresh_token,
            token_type="bearer",
        )


def get_user_service() -> UserService:
    return UserService()


UserServiceDeps = Annotated[UserService, Depends(get_user_service)]
