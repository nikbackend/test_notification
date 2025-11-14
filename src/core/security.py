from datetime import datetime, timedelta, timezone
from typing import Annotated, Literal

import bcrypt
from fastapi import Depends, Header, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt  # type: ignore

from src.core.exceptions import CustomException
from src.core.settings import settings

MAX_BCRYPT_LENGTH = 72
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/auth/login")


def hash_password(password: str) -> str:
    truncated = password[:MAX_BCRYPT_LENGTH]
    return bcrypt.hashpw(truncated.encode(), bcrypt.gensalt()).decode()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    truncated = plain_password[:MAX_BCRYPT_LENGTH]
    return bcrypt.checkpw(truncated.encode(), hashed_password.encode())


def create_auth_token(user_id: str, type_token: Literal["access", "refresh"]) -> str:
    match type_token:
        case "access":
            expire = datetime.now(timezone.utc) + timedelta(
                seconds=settings.JWT.TIME_FOR_ACCESS_TOKEN
            )
        case "refresh":
            expire = datetime.now(timezone.utc) + timedelta(
                seconds=settings.JWT.TIME_FOR_REFRESH_TOKEN
            )
        case _:
            raise CustomException()

    payload = {
        "sub": user_id,
        "type": type_token,
        "iat": datetime.now(timezone.utc),
        "exp": expire,
    }
    return jwt.encode(
        payload,
        settings.JWT.SECRET_KEY.get_secret_value(),
        algorithm=settings.JWT.ALGORITHM,
    )


def verify_token(token: str, token_type: str = "access") -> str:
    try:
        payload = jwt.decode(
            token,
            settings.JWT.SECRET_KEY.get_secret_value(),
            algorithms=[settings.JWT.ALGORITHM],
        )
        if payload.get("type") != token_type:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token type",
            )
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token payload",
            )
        return user_id
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )


async def get_current_user_id(
    access_token: str | None = Header(),
) -> int:
    return verify_token(access_token, token_type="access")


CurrentUserIdDeps = Annotated[int, Depends(get_current_user_id)]
