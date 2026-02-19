from fastapi import FastAPI
from app.routes.health import router as health_router
from app.routes.products import router as product_router
from app.routes.auth import router as auth_router
from app.routes.users import router as user_router

app = FastAPI()

app.include_router(health_router)

app.include_router(product_router)

app.include_router(user_router)

app.include_router(auth_router)