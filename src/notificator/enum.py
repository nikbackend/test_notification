from enum import Enum


class EnumShema(str, Enum):
    LIKE = "like"
    COMMENT = "comment"
    REPOST = "repost"
