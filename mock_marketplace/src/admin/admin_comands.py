from ..posts.database import async_session
from ..posts.models import Products

import asyncio


async def insert_products(name: str, price: int, collection: str | None, discount: int | None, quantity: int, name_for_image: str) -> None:
    async with async_session() as session:
        wear = Products(
            name=name,
            price=price,
            collection=collection,
            discount=discount,
            quantity=quantity,
            name_for_image=name_for_image,
        )

        session.add(wear)
        await session.commit()
