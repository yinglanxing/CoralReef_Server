from fastapi.routing import APIRouter

from .permission import permission_api
from .system import system_api
from .user import user_api

api_router = APIRouter()

# 首页路由
# api_router.include_router(index, prefix="/")

# 用户路由
api_router.include_router(user_api, prefix="/user")

# 系统路由
api_router.include_router(system_api, prefix="/system")

# 权限路由
api_router.include_router(permission_api, prefix="/permission")

# 导出全部路由
__all__ = ['api_router']
