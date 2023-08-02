from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from app import api_router as route_module
from core.config import settings


def createApp():
    app = FastAPI(title=settings.PROJECT_NAME)

    # set middleware
    # register_middleware(app)

    # 挂载路由
    app.include_router(route_module.api_router, prefix="/api/v1")

    # set socketio
    # app.mount('/', socket_app)
    # set static files
    # app.mount("/media", StaticFiles(directory="media"), name="media")  # 媒体文件
    # allow cross domain
    app.add_middleware(CORSMiddleware, allow_origins=settings.BACKEND_CORS_ORIGINS,
                       allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
    # set redis
    # registerRedis(app)
    # set custom exceptions
    # customExceptions(app)
    # # print all path
    # for _route in app.routes:
    #     r = _route.__dict__
    #     print(r['path'], r.get('methods', {}))
    return app


app = createApp()

if __name__ == '__main__':
    import uvicorn

    # Don't set debug/reload equals True in release, because TimedRotatingFileHandler can't support multi-prcoess
    # please used "uvicorn --host 127.0.0.1 --port 8000 main:app --env-file ./configs/.env" run in release,
    # and used "python main.py" in dev
    uvicorn.run(
        app='main:app',
        host=str(settings.HOST),
        port=settings.PORT,
        reload=settings.RELOAD,
        log_config=str(settings.LOGGING_CONFIG_FILE)
    )
