# import json
# import os
# import hashlib

from sqlalchemy import select, func
from src import cfg
from src.db.db import async_session_maker
# from src.log import set_logger
from src.models import M_STA


async def sta_get_all():
    content = {"msg": f"error"}
    # log = set_logger(cfg.AREA_FILE_LOG)

    try:
        async with async_session_maker() as session:
            res = await session.scalars(
                select(M_STA)
                # .order_by(M_NSI_AREA.name_ru)
            )
            _all = res.all()
            cnt = len(_all)
            content = {"msg": cfg.MSG_OK, "count": cnt, "data": _all}
            # log.info("ngp load successfully")
            return content
    except Exception as e:
        cont_err = f"fail. can't read area from table ({M_STA.__tablename__})"
        content = {"msg":cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content


async def sta_get_all_count():
    content = {"msg": f"error"}
    try:
        async with async_session_maker() as session:
            res = await session.scalar(select(func.count(M_STA.id)))
            content = {"msg": cfg.MSG_OK, "count": res}
            return content
    except Exception as e:
        cont_err = f"fail. can't read ext from table ({M_STA.__tablename__})"
        content = {"msg": cfg.MSG_ERROR, "data": f"Exception occurred {str(e)} . {cont_err}"}
        print(content)
    finally:
        if session is not None:
            await session.close()
    return content