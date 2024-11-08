from typing import Annotated

from fastapi import APIRouter, File, UploadFile

import pathlib

from .admin.admin_comands import insert_products


files = Annotated[list[bytes], File()]
router = APIRouter(tags=['insert wear in db'], prefix='/admin')


@router.post('/insert_wear')
async def all_wears(name: str, price: int, quantity: int, files: list[UploadFile],
                    description: str, characteristics: str, colors: str,
                    collection: str = None, discount: int = None):

    path_file = pathlib.Path(__file__).parent / 'frontend' / 'frontend-mock-marketplace' / 'public' / 'images'

    for file in files:
        content_file = await file.read()

        with open(f"{path_file}/{file.filename}", "wb") as f:
            f.write(content_file)

    await insert_products(
        name=name,
        price=price,
        collection=collection,
        discount=discount,
        quantity=quantity,
        description=description,
        characteristics=characteristics,
        colors=colors,

        name_for_image_1=files[0].filename,
        name_for_image_2=files[1].filename,
        name_for_image_3=files[2].filename,
    )

    return f'<h1> You added: {[file.filename for file in files]} </h1>'
