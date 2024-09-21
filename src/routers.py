from fastapi import APIRouter
from src.api.sta.router import sta_router
from src.api.stl.router import stl_router
from src.api.stp.router import stp_router

api_router = APIRouter(prefix='/api/v1')

api_router.include_router(sta_router)
api_router.include_router(stl_router)
api_router.include_router(stp_router)