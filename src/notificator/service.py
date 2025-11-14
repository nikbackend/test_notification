from typing import Annotated

from fastapi import Depends

from src.core.exceptions import NotFoundException
from src.notificator.repo import NotificatorRepo
from src.notificator.shemes import NotificationCreateSchema


class NotificatorService:
    def __init__(self):
        self.repo = NotificatorRepo()

    async def create_notification(self, user_id: int, data: NotificationCreateSchema, conn):
        return await self.repo.create_notification(
            user_id=user_id, type=data.type, text=data.text, conn=conn
        )

    async def delete_notification(self, user_id: int, notification_id: int, conn):
        notification = await self.repo.get_notification(notification_id, user_id, conn)
        if not notification:
            raise NotFoundException("Уведолмение не найдено")

        await self.repo.delete_notification(notification_id, user_id, conn)
        return True

    async def list_notifications(self, user_id: int, limit: int, offset: int, conn):
        return await self.repo.list_notifications(
            user_id=user_id, limit=limit, offset=offset, conn=conn
        )


def get_notificator_service() -> NotificatorService:
    return NotificatorService()


NotificatorServiceDeps = Annotated[NotificatorService, Depends(get_notificator_service)]
