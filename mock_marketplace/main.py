from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from fastapi.middleware.cors import CORSMiddleware

from src.auth.database import User

from src.routers.routers_cart_purchasing import router as purchasing_router
from src.routers.routers_home_stuff_page import router as home_stuff_router
from src.routers.routers_for_wears import router as wears_router
from src.admin_routers import router as admin_router

from src.auth.auth import auth_backend
from src.auth.manager import get_user_manager
# from src.auth.schemas import UserRead, UserCreate

origins = [
    'http://localhost:5173',
    'http://127.0.0.1:5173',
]

app = FastAPI(title='Own Online Market', version='0.1')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(router=admin_router)
app.include_router(router=home_stuff_router)
app.include_router(router=purchasing_router)
app.include_router(router=wears_router)
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

# app.include_router(
#     fastapi_users.get_register_router(UserRead, UserCreate),
#     prefix="/auth",
#     tags=["auth"],
# )
