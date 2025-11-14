from tortoise import fields
from tortoise.models import Model

from src.notificator.enum import EnumShema


class Notificator(Model):
    id = fields.IntField(primary_key=True)
    user = fields.ForeignKeyField(
        "models.User", related_name="notifications", on_delete=fields.CASCADE
    )
    type = fields.CharEnumField(EnumShema)
    text = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
