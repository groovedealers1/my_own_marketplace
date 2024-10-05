from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from ..admin.admin_comands import insert_products

router = APIRouter(tags=['insert wear in db'], prefix='/admin')


@router.get('', response_class=HTMLResponse)
async def all_wears(name: str, price: int, quantity: int, name_for_image: str, collection: str = None, discount: int = None):
    await insert_products(
        name=name,
        price=price,
        collection=collection,
        discount=discount,
        quantity=quantity,
        name_for_image=name_for_image,
    )
    return HTMLResponse(content='<h1> success </h1>')
