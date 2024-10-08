from fastapi import APIRouter, File, UploadFile

import pathlib

from .admin.admin_comands import insert_products

router = APIRouter(tags=['insert wear in db'], prefix='/admin')


@router.post('/insert_wear')
async def all_wears(name: str, price: int, quantity: int, name_for_image: str, collection: str = None, discount: int = None, file: UploadFile = File(...)):

    path_file = pathlib.Path(__file__).parent / 'frontend' / 'public' / 'images'
    print(path_file)

    file.filename = f"{name_for_image}.jpg"
    contents = await file.read()

    with open(f"{path_file}/{file.filename}", "wb") as f:
        f.write(contents)

    await insert_products(
        name=name,
        price=price,
        collection=collection,
        discount=discount,
        quantity=quantity,
        name_for_image=f'./images/{name_for_image}.jpg',
    )

    return '<h1> success </h1>'
