# import fastapi

from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware

from app.core.config import Settings


# @app.get('/')
# def index():
#     return {'data': {'name': 'Rahul'}}


def create_app():
    # 实例化一个FastAPI对象
    app = FastAPI(title=Settings.PROJECT_NAME, version=Settings.PROJECT_VERSION,
                  description=Settings.PROJECT_DESCRIPTION)
    # 注册路由
    app.include_router(APIRouter(), prefix="/api/v1")

    # add middleware
    app.add_middleware(CORSMiddleware, allow_origins=Settings.BACKEND_CORS_ORIGINS,
                       allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
    # 返回app对象
    return app


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        app='main:app',
        host=str(Settings.HOST),
        port=Settings.PORT,
        reload=Settings.RELOAD,
        log_config=Settings.LOGGING_CONFIG_FILE
    )
