from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(primary_key=True)
    username = fields.CharField(max_length=100, unique=True)
    password = fields.CharField(max_length=250)
    avatar_url = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.username
