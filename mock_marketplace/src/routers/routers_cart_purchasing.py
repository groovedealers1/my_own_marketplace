from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter(tags= ['adding to cart and purchasing product'])
templates = Jinja2Templates(directory="src/frontend/template")


@router.get('/cart', response_class=HTMLResponse)
async def cart(request: Request):
    return templates.TemplateResponse(
        request=request, name='cart.html'
    )
