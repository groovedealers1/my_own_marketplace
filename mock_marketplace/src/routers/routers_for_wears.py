from fastapi import APIRouter

from ..posts.orm import get_all_wears, get_wear_by_id

router = APIRouter(tags=['get wear from db'], prefix='/wears')


@router.get('')
async def all_wears():
    return await get_all_wears()


@router.get('/{wear_id}')
async def wear_by_id(wear_id: int = 2):
    return await get_wear_by_id(wear_id)
