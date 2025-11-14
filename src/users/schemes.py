from pydantic import BaseModel, Field, field_validator


class RegistrationSchema(BaseModel):
    username: str = Field(min_length=5, max_length=100)
    avatar_url: str = Field(..., description="URL аватарки")
    password: str = Field(min_length=4)

    @field_validator("password")
    @classmethod
    def check_password_strength(cls, v: str) -> str:
        if len(v) < 4:
            raise ValueError("Пароль должен содержать минимум 6 символов")
        return v


class LoginSchema(BaseModel):
    username: str = Field(min_length=5, max_length=100)
    password: str = Field(min_length=4)


class LoginResponseSchema(BaseModel):
    access_token: str
    token_type: str
    refresh_token: str
    user_id: int
