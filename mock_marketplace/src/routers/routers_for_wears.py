from fastapi import APIRouter
from fastapi.responses import HTMLResponse

import json

from ..posts.orm import get_all_wears, get_wear_by_id

router = APIRouter(tags=['get wear from db'], prefix='/wears')


@router.get('')
async def all_wears():
    return await get_all_wears()


@router.get('/{wear_id}', response_class=HTMLResponse)
async def wear_by_id(wear_id: int = 4):
    return json.dumps(await get_wear_by_id(wear_id), ensure_ascii=False)
