from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" ADD "password" VARCHAR(250) NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" DROP COLUMN "password";"""


MODELS_STATE = (
    "eJztmFtP2zAUx79KlScmMQQdpYi3UMLooC1qw4a4KHITN42a2MVxKBXqd5/txM09KxOMdu"
    "pbcnxOfM7Pt3/8qnjYgq6/d+NDopzUXhUEPMgeUvbdmgKm09jKDRQMXeEYSI+hTwkwKbON"
    "gOtDZrKgbxJnSh2MmBUFrsuN2GSODrJjU4CcpwAaFNuQjkUe94/M7CALvkBfvk4nxsiBrp"
    "VK07F438Ju0PlU2NqIngtH3tvQMLEbeCh2ns7pGKOlt4Mot9oQQQIo5J+nJODp8+yiKmVF"
    "YaaxS5hiIsaCIxC4NFHuigxMjDg/lo0vCrR5L1/rB4fNw+NvR4fHzEVksrQ0F2F5ce1hoC"
    "DQ1ZWFaAcUhB4CY8yNj5p4ztFrjQEpxpeMyUBkqWchSmSfStEDL4YLkU3H7PVgf7+C2U+1"
    "37pQ+zvM6wuvBbPJHM7wbtRUD9s42BjkFPj+DJOCaVgOMhnzPiClISYZr8GPQFlvrIKSeZ"
    "WiFG1plOCZzVZiBMTNw9ThS8miTkdtCs4Kerp2q/OkPd9/cpPQdjrqreDpzaOWq173u3RP"
    "QG5d9U4zbE0Cef0GoHm2Z6yFOh4s5puOzPC1otA9+bCetBVWg9VD7jzaYqrotzvaQFc716"
    "khOFN1jbfUU/ildecoM82XH6n9ausXNf5au+t1NUEQ+9QmosfYT79TeE4goNhAeGYAK7Eb"
    "SqsEs+Cn4WiS2Ne5YQjMyQwQy0i1xDMAYeqMHBNwdn5+EpxG4eeXfegKp4LhjkRBV34Kr/"
    "fqiq1y3DkoXMdl6PJNXt3LWgACtsia9817KqBSoKQy0MoFFco4bnXVBukqUX2hFNBQ4Al8"
    "bZYQQCbMYZSxn3yGKVftS+2k5joT+IBavU5H6+onNRN7HkT0AfW1696AGQjkO5nyF+Khir"
    "A86pqlwqGZlQ2USYO3CAbpv5UKW6nw30uF5MDy/zfjTRt7IuLPu/uajN87bPA5fZVmmAd4"
    "jgl0bHQJ57kdvlhByWuV9eNXJp2YmYDZUikkpwYrjxUFaXjUqYOWeqYpi3JN+pEiTIXEMc"
    "dF+itqqZReIPbZqq41W5RVqusZEj/6Y1n1DiYRsilCIHsF01jpCqZRcQXTyF3BsKXxBoiR"
    "+2YC/JDrQNYjhahAOf0Y9LolqikOyYC8QazAe8sx6S6T4z59XE+sFRR51dUCNatFM7KHf+"
    "C06Ej+l8fL4jcA/g/L"
)
