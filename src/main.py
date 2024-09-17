# uvicorn main:app --reload
# https://habr.com/ru/articles/705752/
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from src import cfg
from src.db.db import get_async_session, engine
from src.routers import api_router

app = FastAPI(title="GDX2 Map BackEnd")

# , root_path=API_VERSION
# origins = [
#     "http://localhost",
#     "http://localhost:8080",
#     "https://localhost",
#     "https://localhost:8080",
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
    "Authorization"],
)


# Root API
@app.get("/", status_code=200,
         name='Get Info',
         tags=['Главная'],
         description='Получает информацию о сервисе')
def root() -> JSONResponse:
    url_swagger = f"http://{cfg.SERVER_HOST}:{cfg.SERVER_PORT}/docs"

    return JSONResponse(status_code=200,
                        content={
                            "msg": "Success",
                            "Info": "Hello it is FastAPI-NSI project",
                            "Swagger Documentation": url_swagger})


app.include_router(api_router)

class Server():
    def __init__(self, as_service=False):
        self._srv = None
        self._svc = None
        self.as_service = as_service

    def start(self):

        # Здесь можно настроить параметры хоста, порта, логирования
        config = uvicorn.Config(app)
        config.host = cfg.SERVER_HOST
        config.port = int(cfg.SERVER_PORT)
        config.reload = True
        config.workers = 4
        
        self._srv = uvicorn.Server(config=config)

        if self.as_service:
            self._srv.install_signal_handlers = lambda: None

        self._srv.run()

    def stop(self):
        if self._srv is not None:
            self._srv.should_exit = True


def run():
    srv = Server()
    srv.start()


if __name__ == "__main__":
    run()
    # set_logger()
    # uvicorn.run("main:app", host=cfg.SERVER_HOST, port=int(cfg.SERVER_PORT), reload=True, workers=4)
