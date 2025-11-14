from fastapi import Request, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

from src.core.exceptions import CustomException
from src.core.settings import log


class LogHandlingMiddleware(BaseHTTPMiddleware):
    """Логирование запросов"""

    async def dispatch(self, request: Request, call_next) -> Response:
        log.info(f"Запрос: {request.method} {request.url.path}?{request.url.query}")
        try:
            response = await call_next(request)
        except CustomException as exc:
            log.warning(f"{request.method} {request.url.path} {exc.status_code} {exc.detail}")
            return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})
        except Exception as exc:
            log.error(f"Ошибка запроса: {request.method} {request.url.path} - {exc}")
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={"detail": "Внутренняя ошибка сервера"},
            )
        log.info(
            f"Результат выполнения: {request.method} {request.url.path} - Status: {response.status_code}"
        )
        return response
