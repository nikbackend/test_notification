from typing import Annotated, AsyncGenerator

from fastapi import Depends
from tortoise.backends.base.client import BaseDBAsyncClient
from tortoise.transactions import in_transaction


async def get_transaction() -> AsyncGenerator[BaseDBAsyncClient, None]:
    async with in_transaction() as conn:
        yield conn


AsyncTransactionDeps = Annotated[BaseDBAsyncClient, Depends(get_transaction)]
