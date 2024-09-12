from fastapi import FastAPI
from src.routers.routers_cart_purchasing import router as purchasing_router
from src.routers.routers_home_stuff_page import router as home_stuff_router


app = FastAPI(debug=True, title='DAMN FUUUCK', version='0.1')

app.include_router(router=home_stuff_router)
app.include_router(router=purchasing_router)
