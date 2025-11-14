from tortoise.backends.base.client import BaseDBAsyncClient

from src.notificator.model import Notificator


class NotificatorRepo:
    async def create_notification(
        self, user_id: int, type: str, text: str, conn: BaseDBAsyncClient
    ):
        notification = await Notificator.create(
            user_id=user_id, type=type, text=text, using_db=conn
        )
        return notification

    async def delete_notification(
        self, notification_id: int, user_id: int, conn: BaseDBAsyncClient
    ):
        deleted_count = (
            await Notificator.filter(id=notification_id, user_id=user_id).using_db(conn).delete()
        )
        return deleted_count

    async def list_notifications(
        self,
        user_id: int,
        limit: int = 10,
        offset: int = 0,
        conn: BaseDBAsyncClient = None,
    ):
        notifications = (
            await Notificator.filter(user_id=user_id).offset(offset).limit(limit).using_db(conn)
        )
        return notifications

    async def get_notification(self, notification_id: int, user_id: int, conn: BaseDBAsyncClient):
        notification = (
            await Notificator.filter(id=notification_id, user_id=user_id).using_db(conn).first()
        )
        return notification
