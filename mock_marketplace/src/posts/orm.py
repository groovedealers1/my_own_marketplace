from sqlalchemy import select

from .database import engine
from .models import Products


async def get_all_wears() -> list:
    async with engine.connect() as conn:
        stmt = select(Products)
        res = await conn.execute(stmt)
        result = res.all()

        list_of_wears = []

        for sset in result:
            list_of_wears.append(list(sset))

        return list_of_wears


async def get_wear_by_id(wear_id: int):
    async with engine.connect() as conn:
        stmt = select(Products).where(Products.id == wear_id)
        res = await conn.execute(stmt)
        result = list(res.all()[0])

        return result
