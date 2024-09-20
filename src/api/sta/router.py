from fastapi import APIRouter
from src.api.sta.services import sta_get_all, sta_get_all_count

sta_router = APIRouter(prefix="/sta", tags=["Отчеты"])

#
@sta_router.get(path='/all',
                status_code=200,
                name='Получить все Отчеты - точки',
                tags=['Отчеты'],
                description='Получает все Отчеты - точки')
async def get_sta_get_all():
    content = await sta_get_all()
    return content
#
#
#
@sta_router.get(path='/count',
                status_code=200,
                name='Получить количество Площадей',
                tags=['Площади'],
                description='Получает количество Площадей')
async def get_sta_get_all_count():
    content = await sta_get_all_count()
    return content
