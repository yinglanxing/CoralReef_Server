import json
from typing import Optional, Dict, Any

from fastapi import FastAPI, status, HTTPException
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.requests import Request

from .error_code import ErrorBase, ERROR_USER_TOKEN_FAILURE, ERROR_PARAMETER_ERROR, ERROR_USER_PREM_ERROR
from .resp import respErrorJson

# 服务端异常处理模块
# 定义了一些自定义异常和异常处理器，用于处理特定类型的异常并返回自定义的错误信息。

def customExceptions(app: FastAPI):
    # 重写HTTPException为项目中需要的返回类型
    @app.exception_handler(StarletteHTTPException)
    # http_exception_handle 是一个异常处理器函数，它用于处理 StarletteHTTPException 类型的异常。
    # 它接受两个参数，request 代表请求对象，exec 代表异常对象。
    # 该处理器会将异常转换为自定义的返回类型，并返回一个包含错误信息的 JSON 响应。
    async def http_exception_handle(request: Request, exec: StarletteHTTPException):
        err = exec.err if hasattr(exec, 'err') else ErrorBase(code=exec.status_code)
        return respErrorJson(error=err, status_code=exec.status_code, msg=exec.detail)

    # 重写RequestValidationError为项目中需要的返回类型

    # http_exception_handle
    # 还定义了一个异常处理器函数，用于处理
    # RequestValidationError类型的异常。
    # 它也接受两个参数，request代表请求对象，exec代表异常对象。
    # 该处理器会将异常转换为自定义的返回类型，并返回一个包含错误信息的SON响应。
    @app.exception_handler(RequestValidationError)
    async def http_exception_handle(request: Request, exec: RequestValidationError):
        err = ERROR_PARAMETER_ERROR
        return respErrorJson(error=err, status_code=err.code, data={'errors': json.loads(exec.json())})


# 是一个自定义的异常类，继承自 HTTPException。它包含一个 err 属性，代表错误信息。它还定义了一个构造函数，用于初始化异常对象。
class CustomErrorBase(HTTPException):
    err: ErrorBase

    def __init__(self, headers: Optional[Dict[str, Any]] = None):
        super().__init__(status_code=status.HTTP_200_OK,
                         detail=self.err.msg,
                         headers=headers)


# UserTokenError 是一个自定义的异常类，继承自 CustomErrorBase。它将 err 属性设置为 ERROR_USER_TOKEN_FAILURE，代表用户令牌错误。
class UserTokenError(CustomErrorBase):
    err = ERROR_USER_TOKEN_FAILURE


# UserPermError 是一个自定义的异常类，继承自 CustomErrorBase。它将 err 属性设置为 ERROR_USER_PREM_ERROR，代表用户权限错误。
class UserPermError(CustomErrorBase):
    err = ERROR_USER_PREM_ERROR
