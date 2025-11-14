from fastapi import HTTPException, status


class CustomException(HTTPException):

    def __init__(
        self,
        detail: str = "Произошла ошибка",
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
    ):
        super().__init__(detail=detail, status_code=status_code)


class NotFoundException(CustomException):
    def __init__(self, detail: str = "Ресурс не найден"):
        super().__init__(detail, status_code=status.HTTP_404_NOT_FOUND)


class ForbiddenException(CustomException):
    def __init__(self, detail: str = "Доступ запрещен"):
        super().__init__(detail, status_code=status.HTTP_403_FORBIDDEN)


class UnauthorizedException(CustomException):
    def __init__(self, detail: str = "Необходимо авторизоваться"):
        super().__init__(detail, status_code=status.HTTP_401_UNAUTHORIZED)


class InvalidTokenException(CustomException):
    def __init__(self, detail: str = "Неверный токен"):
        super().__init__(detail, status_code=status.HTTP_401_UNAUTHORIZED)


class ExistsException(CustomException):
    def __init__(self, detail: str = "Этот объект уже существует"):
        super().__init__(detail=detail, status_code=status.HTTP_400_BAD_REQUEST)


class NoChangesException(CustomException):
    def __init__(
        self,
        detail: str = "Объект не был изменён",
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
    ):
        super().__init__(detail, status_code)


class NoCreateException(CustomException):
    def __init__(
        self,
        detail: str = "Ошибка при создании ресурса",
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
    ):
        super().__init__(detail, status_code)


class InvalidCodeException(CustomException):
    def __init__(
        self,
        detail: str = "Неверные учетные данные",
        status_code: int = status.HTTP_400_BAD_REQUEST,
    ):
        super().__init__(detail, status_code)


class BadRequestException(CustomException):
    def __init__(
        self,
        detail: str = "Некорректный запрос",
        status_code: int = status.HTTP_400_BAD_REQUEST,
    ):
        super().__init__(detail, status_code)


class ConflictException(CustomException):
    def __init__(self, detail: str = "", status_code: int = status.HTTP_409_CONFLICT):
        super().__init__(detail, status_code)
