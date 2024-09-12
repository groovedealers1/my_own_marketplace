from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


router = APIRouter(tags=['catalog'])
templates = Jinja2Templates(directory="src/frontend/template")


@router.get('/', response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse(
        request=request, name='home_page.html'
    )

@router.get('/stuff_page', response_class=HTMLResponse)
async def stuff_page(request: Request):
    return templates.TemplateResponse(
        request=request, name='stuff_page.html'
    )