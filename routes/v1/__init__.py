from fastapi import APIRouter

# from .users import users_router

v1_router = APIRouter()

# v1_router.include_router(users_router, prefix="/users", tags=["users"])

@v1_router.get("/")
async def route_root():
    return {"Hello": "World"}
