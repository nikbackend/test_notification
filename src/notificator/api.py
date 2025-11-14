from fastapi import APIRouter, status

from src.core.exceptions import NotFoundException
from src.core.security import CurrentUserIdDeps
from src.core.session import AsyncTransactionDeps
from src.notificator.shemes import NotificationCreateSchema, NotificationSchema

from .service import NotificatorService

router = APIRouter(prefix="/notifications", tags=["notifications"])
service = NotificatorService()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=NotificationSchema)
async def create_notification(
    data: NotificationCreateSchema,
    db: AsyncTransactionDeps,
    user_id: CurrentUserIdDeps,
):
    return await service.create_notification(user_id=user_id, data=data, conn=db)


@router.delete("/{notification_id}")
async def delete_notification(
    notification_id: int,
    user_id: CurrentUserIdDeps,
    db: AsyncTransactionDeps,
):
    await service.delete_notification(user_id=user_id, notification_id=notification_id, conn=db)
    return {"detail": "Уведомление удалено"}


@router.get("/", response_model=list[NotificationSchema])
async def list_notifications(
    user_id: CurrentUserIdDeps,
    db: AsyncTransactionDeps,
    limit: int = 10,
    offset: int = 0,
):
    notifications = await service.list_notifications(
        user_id=user_id, limit=limit, offset=offset, conn=db
    )
    if not notifications:
        raise NotFoundException("Уведомления не найдены")
    return notifications
