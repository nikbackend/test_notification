from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from tortoise.backends.base.client import BaseDBAsyncClient

from src.core.session import get_transaction
from src.users.service import UserRepo, UserService

AsyncTransactionDeps = Annotated[BaseDBAsyncClient, Depends(get_transaction)]


def get_user_repo() -> UserRepo:
    return UserRepo()


def get_user_service(repo: UserRepo = Depends(get_user_repo)) -> UserService:
    return UserService(repo)


UserServiceDeps = Annotated[UserService, Depends(get_user_service)]

OAuth2FormDeps = Annotated[OAuth2PasswordRequestForm, Depends()]
