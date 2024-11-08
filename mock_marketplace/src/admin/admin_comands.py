from ..posts.database import async_session
from ..posts.models import Products, Images


async def insert_products(name: str, price: int, collection: str | None, discount: int | None, quantity: int,
                          description: str, characteristics: str, colors: str,
                          name_for_image_1: str, name_for_image_2: str, name_for_image_3: str) -> None:

    async with async_session() as session:
        wear = Products(
            name=name,
            price=price,
            collection=collection,
            discount=discount,
            quantity=quantity,
            description=description,
            characteristics=characteristics,
            colors=colors,
        )

        image = Images(
            name_for_image_1=name_for_image_1,
            name_for_image_2=name_for_image_2,
            name_for_image_3=name_for_image_3
        )

        session.add_all([wear, image])
        await session.commit()
