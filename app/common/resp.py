from typing import Union, Optional

from app.common.error_code import ErrorBase

from fastapi import status
from fastapi.responses import JSONResponse  # , ORJSONResponse
from pydantic import BaseModel


class respJsonBase(BaseModel):
    code: int
    msg: str
    data: Union[dict, list]


# 以下两个方法用于处理接口的成功和错误响应
def respSuccessJson(data: Union[list, dict, str] = None, msg: str = "Success"):
    """ 接口成功返回 """
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'code': 0,
            'msg': msg,
            'data': data or {}
        }
    )


def respErrorJson(error: ErrorBase, *, msg: Optional[str] = None, msg_append: str = "",
                  data: Union[list, dict, str] = None, status_code: int = status.HTTP_200_OK):
    """ 错误接口返回 """
    return JSONResponse(
        status_code=status_code,
        content={
            'code': error.code,
            'msg': (msg or error.msg) + msg_append,
            'data': data or {}
        }
    )
