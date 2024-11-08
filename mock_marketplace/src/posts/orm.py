from typing import Any

from sqlalchemy import select

from .database import engine
from .models import Products, Images


async def get_all_images() -> list[dict[str, Any]]:
    async with engine.connect() as conn:
        stmt = select(Images)
        res = await conn.execute(stmt)
        result = res.all()

        list_of_images = []
        list_of_named = ["id", "name_for_image_1", "name_for_image_2", "name_for_image_3"]

        for i in range(len(result)):
            x = {}
            for u in range(len(result[i])):
                x[list_of_named[u]] = result[i][u]

            list_of_images.append(x)

        return list_of_images



async def get_images_by_id(images_id) -> dict[str, Any]:
    async with engine.connect() as conn:
        stmt = select(Images).where(images_id == Images.id)
        res = await conn.execute(stmt)

        list_of_named = ["id", "name_for_image_1", "name_for_image_2", "name_for_image_3"]

        try:
            wear_data = res.all()[0]
            wear_dict = {list_of_named[i]: wear_data[i] for i in range(len(wear_data))}
        except IndexError:
            wear_dict = {'data': None}

        return wear_dict


async def get_all_wears() -> list[dict[str, Any]]:
    async with engine.connect() as conn:
        stmt = select(Products)
        res = await conn.execute(stmt)
        result = res.all()

        all_images = await get_all_images()


        list_of_wears = []
        list_of_named = ["id", "name", "description",
                         "characteristics", "colors", "price",
                         "collection", "discount", "quantity"]

        for i in range(len(result)):
            x = {}
            for u in range(len(result[i])):
                x[list_of_named[u]] = result[i][u]

            x['images'] = all_images[i]

            list_of_wears.append(x)

        return list_of_wears


async def get_wear_by_id(wear_id: int) -> dict[str, int | str | None]:
    async with engine.connect() as conn:
        stmt = select(Products).where(wear_id == Products.id)
        res = await conn.execute(stmt)
        wear_images = await get_images_by_id(wear_id)

        list_of_named = ["id", "name", "description",
                         "characteristics", "colors", "price",
                         "collection", "discount", "quantity"]

        wear_data = res.all()[0]
        wear_dict = {list_of_named[i]: wear_data[i] for i in range(len(wear_data))}

        wear_dict['images'] = wear_images

        return wear_dict
