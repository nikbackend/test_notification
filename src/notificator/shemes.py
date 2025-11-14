from datetime import datetime

from pydantic import BaseModel

from src.notificator.enum import EnumShema


class NotificationCreateSchema(BaseModel):
    type: EnumShema
    text: str


class NotificationSchema(BaseModel):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True
