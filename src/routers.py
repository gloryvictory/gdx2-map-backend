from fastapi import APIRouter
from src.api.sta.router import sta_router

api_router = APIRouter(prefix='/api/v1')

api_router.include_router(sta_router)