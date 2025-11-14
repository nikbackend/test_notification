from fastapi import APIRouter, status

from src.core.session import AsyncTransactionDeps
from src.users.schemes import LoginResponseSchema, LoginSchema, RegistrationSchema
from src.users.service import UserServiceDeps

router = APIRouter(prefix="/users", tags=["users"])


@router.post(
    "/auth/register",
    status_code=status.HTTP_201_CREATED,
    response_model=LoginResponseSchema,
)
async def register_user(
    data: RegistrationSchema,
    service: UserServiceDeps,
    conn: AsyncTransactionDeps,
):
    return await service.create_user(data, db=conn)


@router.post("/auth/login", response_model=LoginResponseSchema)
async def login_user(
    data: LoginSchema,
    service: UserServiceDeps,
    conn: AsyncTransactionDeps,
):
    return await service.login_user(data.username, data.password, db=conn)
