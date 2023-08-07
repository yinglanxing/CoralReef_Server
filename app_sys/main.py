from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
# 导入路由模块
from app_sys import api_router as route_module
# 导入异常处理模块
from app_sys.common.exceptions import customExceptions

# 上游aioredis库存在基类重复继承问题，故暂时停用此模块。
# 等待上游修复后再启用。
# from app.db.cache import registerRedis

from app_sys.configs.config import settings


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
    # 注册 redis 缓存池模块
    # registerRedis(app)

    # 注册异常处理模块
    customExceptions(app)
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
        log_config=str(settings.LOGGING_CONFIG_FILE)  # 日志配置文件,如不需要日志可注释掉
    )
