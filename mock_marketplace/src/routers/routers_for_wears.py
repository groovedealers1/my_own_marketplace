from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
# from fastapi.templating import Jinja2Templates

import json

from ..posts.orm import get_all_wears, get_wear_by_id

router = APIRouter(tags=['get wear from db'], prefix='/wears')


@router.get('', response_class=HTMLResponse)
async def all_wears():
    return json.dumps(await get_all_wears(), ensure_ascii=False)


@router.get('/{wear_id}', response_class=HTMLResponse)
async def wear_by_id(wear_id: int = 4):
    return json.dumps(await get_wear_by_id(wear_id), ensure_ascii=False)