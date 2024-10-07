from typing import Dict, Any, Set, Tuple, Sequence, List

from sqlalchemy import select, Row

from .database import engine
from .models import Products


async def get_all_wears() -> list[dict[str, Any]]:
    async with engine.connect() as conn:
        stmt = select(Products)
        res = await conn.execute(stmt)
        result = res.all()
        print(result)

        list_of_wears = []
        list_of_named = ["id", "name", "price", "collection", "discount", "quantity", "imageSrc"]

        for i in range(len(result)):
            x = {}
            for u in range(len(result[i])):
                x[list_of_named[u]] = result[i][u]

            list_of_wears.append(x)

        return list_of_wears


async def get_wear_by_id(wear_id: int):
    async with engine.connect() as conn:
        stmt = select(Products).where(wear_id == Products.id)
        res = await conn.execute(stmt)

        list_of_named = ["id", "name", "price", "collection", "discount", "quantity", "imageSrc"]

        wear_data = res.all()[0]
        wear_dict = {list_of_named[i]: wear_data[i] for i in range(len(wear_data))}

        return wear_dict
