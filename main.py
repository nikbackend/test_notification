import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from src.core.middleware import LogHandlingMiddleware
from src.core.settings import TORTOISE_ORM, settings
from src.notificator.api import router as notificator_router
from src.users.api import router as users_router

app = FastAPI(title="Notificator API")


app.add_middleware(LogHandlingMiddleware)

app.include_router(users_router)
app.include_router(notificator_router)

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=False,
    add_exception_handlers=False,  # Отключаем дефолтные обработчики Tortoise
)

if __name__ == "__main__":
    uvicorn.run(app, host=settings.APP.HOST, port=settings.APP.PORT)
