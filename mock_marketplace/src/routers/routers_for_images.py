from fastapi import APIRouter

from ..posts.orm import get_all_images, get_images_by_id

router = APIRouter(tags=['get image/images from db'], prefix='/images')


@router.get('')
async def all_images():
    return await get_all_images()


@router.get('/{image_id}')
async def get_images(image_id: int):
    return await get_images_by_id(image_id)
