from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = Path(__file__).parent.parent
ENV_FILE = ROOT_DIR / ".env"


class DefaultSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        extra="ignore",
    )


class AppSettings(DefaultSettings):
    HOST: str = "localhost"
    PORT: int = 8000


class DataBaseSettings(DefaultSettings):
    POSTGRES_DB: str = "db_notificator"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: SecretStr = SecretStr("postgres")
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"
    POSTGRES_DB_TEST: str = "db_notificator_test"

    @property
    def db_domain(self) -> SecretStr:
        return SecretStr(
            f"{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD.get_secret_value()}@"
            f"{self.DB_HOST}:"
            f"{self.DB_PORT}/"
            f"{self.POSTGRES_DB}",
        )

    @property
    def sync_db_url(self) -> SecretStr:
        return SecretStr(f"postgresql://{self.db_domain.get_secret_value()}")

    @property
    def async_db_url(self) -> SecretStr:
        return SecretStr(f"asyncpg://{self.db_domain.get_secret_value()}")


class JWTSettings(DefaultSettings):
    model_config = SettingsConfigDict(env_prefix="JWT_")
    SECRET_KEY: SecretStr = SecretStr("secret_key")
    TIME_FOR_ACCESS_TOKEN: int = 900
    TIME_FOR_REFRESH_TOKEN: int = 86400
    ALGORITHM: str = "HS256"


class TestDataBaseSettings(DataBaseSettings):
    """Настройки только для тестовой базы данных"""

    @property
    def async_db_url_test(self) -> str:
        """Асинхронный URL для тестовой БД"""
        return f"asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD.get_secret_value()}@{self.DB_HOST}:{self.DB_PORT}/{self.POSTGRES_DB_TEST}"

    @property
    def sync_db_url_test(self) -> str:
        """Синхронный URL для тестовой БД"""
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD.get_secret_value()}@{self.DB_HOST}:{self.DB_PORT}/{self.POSTGRES_DB_TEST}"


class Settings(DefaultSettings):
    APP: AppSettings = AppSettings()
    DATABASE: DataBaseSettings = DataBaseSettings()
    JWT: JWTSettings = JWTSettings()


settings = Settings()
test_db_settings = TestDataBaseSettings()

TEST_TORTOISE_ORM = {
    "connections": {"default": test_db_settings.async_db_url_test},
    "apps": {
        "models": {
            "models": ["src.users.model", "src.notificator.model"],
            "default_connection": "default",
        }
    },
}


TORTOISE_ORM = {
    "connections": {"default": settings.DATABASE.async_db_url.get_secret_value()},
    "apps": {
        "models": {
            "models": ["src.users.model", "src.notificator.model"],
            "default_connection": "default",
        }
    },
}

import logging

# Настройка логгера
log = logging.getLogger("notificator")
log.setLevel(logging.DEBUG)

# Консольный хендлер
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
console_handler.setFormatter(formatter)

log.addHandler(console_handler)
