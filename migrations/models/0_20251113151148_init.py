from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(100) NOT NULL UNIQUE,
    "avatar_url" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "notificator" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "type" VARCHAR(7) NOT NULL,
    "text" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "notificator"."type" IS 'LIKE: like\nCOMMENT: comment\nREPOST: repost';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztmFtP2zAUx79KlScmMQQdUMRbKGF00Ba1YUNcFLmJm1pN7OI4QIX63Wc7cXPPYIJRpr"
    "415xKf8/Pt3zxrPnGgF2xdBpBqh41nDQMf8h8Z+2ZDA7NZYhUGBkaeDAxVxChgFNiM28bA"
    "CyA3OTCwKZoxRDC34tDzhJHYPBBhNzGFGN2H0GLEhWwi67i542aEHfgEA/U4m1pjBD0nUy"
    "ZyxNjSbrH5TNo6mJ3IQDHayLKJF/o4CZ7N2YTgZTTCTFhdiCEFDIrXMxqK8kV1cZeqo6jS"
    "JCQqMZXjwDEIPZZq94UMbIIFP15NIBt0xShfmzu7rd2Db/u7BzxEVrK0tBZRe0nvUaIk0D"
    "O1hfQDBqIIiTHhJmZN/i7Qa08ALceXzslB5KXnISpkH0rRB0+WB7HLJvxxZ3u7htlPfdA+"
    "1QcbPOqL6IXwxRyt8F7sakY+ATYBCR44YmqF1CuiNOFTxUrMZr0NTGVIaCb78G1w1tAzjS"
    "tTFO0Hwb2XhrbR1a8kT38ee877ve8qPAW5fd4/yrG1KRT9W4AV2R5zD0M+LOebzczxdeLU"
    "LfVjNWlrvAenj715vC/q6He6xtDUuxeZKTjWTUN4mhn8yrqxn1vmy5c0fnXM04Z4bFz3e4"
    "YkSALmUjliEmdea6ImEDJiYfJoASe1hZVVgVmII3w8TR1GwjAC9vQRUMfKeJIVgAlDY2QD"
    "wS4oLoKjOP3kbAA9GVQy3fFN1lOvIqu9uxKrmncBijRJFbqiy2/6eQvAwJVVi7HFSCVUSq"
    "7/HLRqFYBzgWsx8InEgOy+VAgYOPQlvg4vCGAbFjCq3A++w7Tzzplx2PDQFN7idr/bNXrm"
    "YcMmvg8xu8UD46I/5AYKxUmm/YV4qCOsrrpWpXBo5WUD49LgNYJBxa+lwloq/PdSIT2x4k"
    "+H9aqDPZXx59N9RebvDQ74gr7KMiwCPCEUIhefwXnhhC9XUOpbwOrxq5JO3EzB41IppJcG"
    "b483BVl01enDtn5saItqTfqeIkyHFNmTMv0Ve2qlF0hi1qprxTZlnep6gDSI/7G89AtMKu"
    "WzCIGsimru7b1AR/GoSiUlfblPMHxrvAJiHP45Ab7LNyw+IoO4RDn9GPZ7FaopScmBvMS8"
    "wRsH2WyTy/GA3a0m1hqKout6gZrXojnZI15wVHYl/8vrZfEbbQmmJw=="
)
